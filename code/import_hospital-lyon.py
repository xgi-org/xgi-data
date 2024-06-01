from datetime import datetime, timedelta

import networkx as nx
import pandas as pd

import xgi

data_folder = "data"

dataset_name = "hospital-lyon"
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


xgi.write_json(H, "data/hospital-lyon/hospital-lyon.json")
