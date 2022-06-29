import xgi
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np


output_stats = True
output_file = True

data = pd.read_csv("data/hospital-lyon/detailed_list_of_contacts_Hospital.dat", sep="\t", header=0, names=["time", "node1", "node2", "type1", "type2"])

edges = dict()
node_dict = dict()
for index, row in data.iterrows():
    time = row["time"]
    node1 = row["node1"]
    node2 = row["node2"]
    type1 = row["type1"]
    type2 = row["type2"]
    e = {node1, node2}

    if node1 not in node_dict:
        node_dict[node1] = type1
    if node2 not in node_dict:
        node_dict[node2] = type2

    if time not in edges:
        edges[time] = [e]
    else:
        flag = True
        for edge in edges[time]:
            if len(edge.intersection(e)) > 0:
                edge.update(e)
                flag = False
                break
        if flag:
            edges[time].append(e)

H = xgi.Hypergraph()
H["name"] = "hospital-Lyon"

for n, type in node_dict.items():
    H.add_node(n, type=type)

start_time = datetime(2010, 12, 6, 13, 0, 0)
for t, edgelist in edges.items():
    time = timedelta(seconds=t)
    H.add_edges_from(edgelist, timestamp=(start_time + time).isoformat())


if output_file:
    xgi.write_hypergraph_json(H, "data/hospital-lyon/hospital-Lyon.json")

if output_stats:
    print((H.num_nodes, H.num_edges))

    print([len(c) for c in xgi.connected_components(H)])

    plt.figure(figsize=(8, 4))
    plt.subplot(121)

    degrees, counts = np.unique(H.nodes.degree.asnumpy(), return_counts=True)
    plt.loglog(degrees, counts / H.num_nodes, "ko", markersize=2)
    plt.title("Degree distribution")
    plt.xlabel(r"$k$", fontsize=16)
    plt.ylabel(r"$P(k)$", fontsize=16)
    plt.subplot(122)
    sizes, counts = np.unique(H.edges.size.asnumpy(), return_counts=True)
    plt.loglog(sizes, counts / H.num_edges, "ko", markersize=2)
    plt.title("Edge size distribution")
    plt.xlabel(r"$m$", fontsize=16)
    plt.ylabel(r"$P(m)$", fontsize=16)
    plt.tight_layout()
    plt.savefig("data/hospital-lyon/stats.png", dpi=300)
    plt.show()