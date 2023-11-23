from datetime import datetime, timedelta

import networkx as nx
import pandas as pd
import xgi

dataset_name = "Hypertext-conference"
data = pd.read_csv(
    "data/Hypertext2009/ht09_contact_list.dat",
    sep="\t",
    header=0,
    names=["time", "node1", "node2"],
)

H = xgi.Hypergraph()
H["name"] = dataset_name

nodes1 = data["node1"].values.tolist()
nodes2 = data["node2"].values.tolist()
nodes = set()
nodes.update(set(nodes))
nodes.update(set(nodes2))

H.add_nodes_from(nodes)

start_time = datetime(2009, 6, 29, 8, 0, 0)

for t in data["time"].unique():
    time = timedelta(seconds=int(t))
    d = data[data.time == t]
    links = d[["node1", "node2"]].values.tolist()
    G = nx.Graph(links)
    for e in nx.find_cliques(G):
        H.add_edge(e, timestamp=(start_time + time).isoformat())


xgi.write_json(H, f"data/Hypertext2009/hypertext-conference.json")
