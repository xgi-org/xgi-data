from datetime import datetime, timedelta

import networkx as nx
import pandas as pd

import xgi

dataset_name = "SFHH-conference"
data = pd.read_csv(
    "data/SFHH/tij_SFHH.dat",
    sep=" ",
    header=0,
    names=["time", "node1", "node2"],
)

H = xgi.Hypergraph()
H["name"] = "SFHH-conference"

nodes1 = data["node1"].values.tolist()
nodes2 = data["node2"].values.tolist()
nodes = set()
nodes.update(set(nodes1))
nodes.update(set(nodes2))

H.add_nodes_from(nodes)

start_time = datetime(2009, 6, 4)

for t in data["time"].unique():
    time = timedelta(seconds=int(t))
    d = data[data.time == t]
    links = d[["node1", "node2"]].values.tolist()
    G = nx.Graph(links)
    for e in nx.find_cliques(G):
        H.add_edge(e, timestamp=(start_time + time).isoformat())


xgi.write_json(H, "data/SFHH/sfhh-conference.json")
