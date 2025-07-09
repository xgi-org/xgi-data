import json

import xgi

H = xgi.Hypergraph()
with open("arxiv-metadata-oai-snapshot.json") as f:
    for line in f:
        try:
            entry = json.loads(line)
        except:
            break
        edge = []
        for author in entry["authors_parsed"]:
            edge.append(
                f"{author[1]} {author[2] + " " if author[2] else ""}{author[0]}"
            )
        H.add_edge(
            edge,
            idx=entry["id"],
            submitter=entry["submitter"],
            title=entry["title"],
            comments=entry["comments"],
            categories=entry["categories"].split(" "),
            abstract=entry["abstract"],
            date=entry["update_date"],
        )

xgi.write_hif(H, "arxiv.json")
