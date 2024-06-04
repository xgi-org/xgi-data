from datetime import datetime, timedelta

import networkx as nx
import pandas as pd
import utilities

import xgi

dataset_name = "InVS15"
data = pd.read_csv(
    "data/InVS15/tij_InVS15.dat",
    sep=" ",
    header=0,
    names=["time", "node1", "node2"],
)

H = xgi.Hypergraph()
H["name"] = "InVS15"

node_labels = utilities.readScHoLPLabels("data/InVS15/metadata_InVS15.txt", "\t")

H.add_nodes_from(node_labels)

H.set_node_attributes(node_labels, name="department")
start_time = datetime(2013, 6, 24)

for t in data["time"].unique():
    time = timedelta(seconds=int(t))
    d = data[data.time == t]
    links = d[["node1", "node2"]].astype(str).values.tolist()
    G = nx.Graph(links)
    for e in nx.find_cliques(G):
        H.add_edge(e, timestamp=(start_time + time).isoformat())

xgi.write_json(H, "data/InVS15/InVS15.json")
