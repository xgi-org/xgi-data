"""
import_cs-cocitations.py

This script constructs the 'cs-cocitations' hypergraph directly from
raw OpenAlex data and exports it in the XGI HIF JSON format.

The resulting hypergraph contains:
- Nodes: highly cited Computer Science papers (top 10% by cumulative
  citations per subfield, minimum 100 papers per subfield).
- Hyperedges: subsets of these highly cited papers that are co-cited
  by at least 3 other papers in the OpenAlex corpus.

Raw data files required (place in the same directory as this script):
  - openalex_work_data_Computer Science.pickle  (OpenAlex Snapshot 2024-09-27)
  - openalex_topic_data.pickle                  (OpenAlex Snapshot 2024-09-27)

Running this script will reproduce the XGI-compatible JSON file:
  cs-cocitations.json
"""

import pickle
from collections import defaultdict
from datetime import datetime
import xgi

# ── Parameters ────────────────────────────────────────────────────────────────
FIELD                   = "Computer Science"
HYPERGRAPH_NAME         = "cs-cocitations"
TOP_PROP                = 0.1    # top fraction by cumulative citations per subfield
MIN_PUB_YEAR            = 1950
MAX_PUB_YEAR            = 2024
MIN_COCITATION_FREQ     = 3
MAX_HYPEREDGE_SIZE      = float('inf')
MIN_PAPERS_PER_SUBFIELD = 100
OPENALEX_SNAPSHOT       = "OpenAlex Snapshot (2024-09-27)"
# ──────────────────────────────────────────────────────────────────────────────

print(f"Loading raw data ({OPENALEX_SNAPSHOT}) ...")

with open(f"openalex_work_data_{FIELD}.pickle", "rb") as f:
    work_data = pickle.load(f)
print(f"  {len(work_data):,} papers loaded for field '{FIELD}'")

with open("openalex_topic_data.pickle", "rb") as f:
    topic_data = pickle.load(f)

# Collect subfields belonging to FIELD
subfields = set()
for t_id in topic_data:
    if topic_data[t_id]["field"]["display_name"] == FIELD:
        subfields.add(topic_data[t_id]["subfield"]["display_name"])
print(f"  {len(subfields)} subfields found")

# ── Step 1: filter papers by publication year, title, and subfield ────────────
invalid_titles = {"none", "", "deleted work"}
work_subfield = {}
for w_id, w in work_data.items():
    pub_y = int(datetime.strptime(str(w["pub_d"]), '%Y-%m-%d').year)
    if pub_y < MIN_PUB_YEAR or pub_y > MAX_PUB_YEAR:
        continue
    title = w["title"]
    if len(title) <= 0 or title in invalid_titles:
        continue
    sf = topic_data[w["t_id"]]["subfield"]["display_name"]
    if sf not in subfields:
        continue
    work_subfield[w_id] = sf

# ── Step 2: count in-field citations for each paper ───────────────────────────
w_ids = set(work_data.keys())
work_cited = defaultdict(int)
for w in work_data.values():
    for ref in set(w["refs"]) & w_ids:
        work_cited[ref] += 1

# ── Step 3: select top papers per subfield as nodes ───────────────────────────
works_by_sf = defaultdict(list)
for w_id, sf in work_subfield.items():
    works_by_sf[sf].append((w_id, work_cited[w_id]))

top_works = []
for sf in subfields:
    sorted_papers = sorted(works_by_sf[sf], key=lambda x: x[1], reverse=True)
    if not sorted_papers:
        continue
    threshold = sum(p[1] for p in sorted_papers) * TOP_PROP
    selected, cumulative = [], 0
    for w_id, count in sorted_papers:
        selected.append(w_id)
        cumulative += count
        if cumulative >= threshold:
            break
    if len(selected) < MIN_PAPERS_PER_SUBFIELD and len(sorted_papers) >= MIN_PAPERS_PER_SUBFIELD:
        selected = [p[0] for p in sorted_papers[:MIN_PAPERS_PER_SUBFIELD]]
    top_works.extend(selected)

top_works = set(top_works)
print(f"  {len(top_works):,} top papers selected as nodes")

# ── Step 4: build co-citation hyperedges ──────────────────────────────────────
cocitation_freq = defaultdict(int)
for w_id, w in work_data.items():
    if w_id in top_works:
        continue
    pub_y = int(datetime.strptime(str(w["pub_d"]), '%Y-%m-%d').year)
    if pub_y < MIN_PUB_YEAR or pub_y > MAX_PUB_YEAR:
        continue
    cited_top = set(w["refs"]) & top_works
    if len(cited_top) < 2 or len(cited_top) > MAX_HYPEREDGE_SIZE:
        continue
    cocitation_freq[tuple(sorted(cited_top))] += 1

hyperedges = [e for e, freq in cocitation_freq.items() if freq >= MIN_COCITATION_FREQ]
print(f"  {len(hyperedges):,} hyperedges (min co-citation freq = {MIN_COCITATION_FREQ})")

# ── Step 5: assign integer node indices (only nodes appearing in hyperedges) ──
nodes_in_edges = set()
for e in hyperedges:
    nodes_in_edges.update(e)

node_list = sorted(nodes_in_edges)          # sorted OpenAlex IDs → deterministic ordering
paper_id_to_idx = {w_id: str(i) for i, w_id in enumerate(node_list)}

# ── Step 6: build XGI Hypergraph ──────────────────────────────────────────────
H = xgi.Hypergraph()

for e in hyperedges:
    H.add_edge(sorted([paper_id_to_idx[w_id] for w_id in e]))

node_data = []
num_invalid = 0
for i, w_id in enumerate(node_list):
    w = work_data[w_id]
    pt = topic_data.get(w["t_id"])
    if pt is None:
        num_invalid += 1
        continue
    pub_d = str(w["pub_d"])
    node_data.append((
        str(i),
        {
            "name":                w_id,
            "openalex_id":         w_id,
            "title":               w["title"],
            "pub_date":            pub_d,
            "year":                int(datetime.strptime(pub_d, '%Y-%m-%d').year),
            "primary_topic_name":  pt["topic_name"],
            "primary_subfield":    pt["subfield"]["display_name"],
            "primary_field":       pt["field"]["display_name"],
            "primary_domain":      pt["domain"]["display_name"],
            "cited_by_count":      int(work_cited[w_id]),
            "source":              OPENALEX_SNAPSHOT,
        }
    ))

H.add_nodes_from(node_data)

N = len(node_list)
M = len(hyperedges)
print(f"\nNumber of papers (nodes):  {N}")
print(f"Number of invalid papers:  {num_invalid}")
print(f"Number of hyperedges:      {M}")

xgi.write_hif(H, f"{HYPERGRAPH_NAME}.json")
print(f"\nSaved: {HYPERGRAPH_NAME}.json")
