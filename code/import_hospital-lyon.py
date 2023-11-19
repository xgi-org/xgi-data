from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import xgi

output_stats = True
output_file = True

data = pd.read_csv(
    "data/hospital-lyon/detailed_list_of_contacts_Hospital.dat",
    sep="\t",
    header=0,
    names=["time", "node1", "node2", "type1", "type2"],
)

H = xgi.Hypergraph()
H["name"] = "hospital-lyon"

nodes1 = dict(zip(data["node1"].values.tolist(), data["type1"].values.tolist()))
nodes2 = dict(zip(data["node2"].values.tolist(), data["type2"].values.tolist()))
nodes = dict()
nodes.update(nodes1)
nodes.update(nodes2)

for node, nodetype in nodes.items():
    H.add_node(node, type=nodetype)

start_time = datetime(2010, 12, 6, 13, 0, 0)

for t in data["time"].unique():
    time = timedelta(seconds=int(t))
    d = data[data.time == t]
    links = d[["node1", "node2"]].values.tolist()
    G = nx.Graph(links)
    for e in nx.find_cliques(G):
        H.add_edge(e, timestamp=(start_time + time).isoformat())


if output_file:
    xgi.write_json(H, "data/hospital-lyon/hospital-lyon.json")

if output_stats:
    print((H.num_nodes, H.num_edges))

    vals, counts = np.unique(
        [len(c) for c in xgi.connected_components(H)], return_counts=True
    )
    print(np.array([vals, counts]))

    plt.figure(figsize=(8, 4))
    plt.subplot(121)

    degrees, counts = np.unique(H.nodes.degree.asnumpy(), return_counts=True)
    plt.plot(degrees, counts / H.num_nodes, "ko", markersize=2)
    plt.title("Degree distribution")
    plt.xlabel(r"$k$", fontsize=16)
    plt.ylabel(r"$P(k)$", fontsize=16)
    plt.subplot(122)
    sizes, counts = np.unique(H.edges.size.asnumpy(), return_counts=True)
    plt.semilogy(sizes, counts / H.num_edges, "ko", markersize=2)
    plt.title("Edge size distribution")
    plt.xlabel(r"$m$", fontsize=16)
    plt.ylabel(r"$P(m)$", fontsize=16)
    plt.tight_layout()
    plt.savefig("data/hospital-lyon/stats.png", dpi=300)
    plt.show()
