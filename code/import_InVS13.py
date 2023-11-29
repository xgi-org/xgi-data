from datetime import datetime, timedelta

import networkx as nx
import pandas as pd
import utilities
import xgi

dataset_name = "InVS13"
data = pd.read_csv(
    "data/InVS13/tij_InVS.dat",
    sep=" ",
    header=0,
    names=["time", "node1", "node2"],
)

H = xgi.Hypergraph()
H["name"] = "InVS13"

nodes1 = data["node1"].astype(str).values.tolist()
nodes2 = data["node2"].astype(str).values.tolist()
nodes = set()
nodes.update(set(nodes1))
nodes.update(set(nodes2))

H.add_nodes_from(nodes)
node_labels = utilities.readScHoLPLabels("data/InVS13/metadata_InVS13.txt", "\t")
H.set_node_attributes(node_labels, name="department")

start_time = datetime(2013, 6, 24)

for t in data["time"].unique():
    time = timedelta(seconds=int(t))
    d = data[data.time == t]
    links = d[["node1", "node2"]].astype(str).values.tolist()
    G = nx.Graph(links)
    for e in nx.find_cliques(G):
        H.add_edge(e, timestamp=(start_time + time).isoformat())

xgi.write_json(H, "data/InVS13/InVS13.json")
