from datetime import datetime, timedelta

import networkx as nx
import pandas as pd
import xgi

dataset_name = "Malawi-village"
data = pd.read_csv(
    "data/Malawi21/tnet_malawi_pilot.csv",
    sep=",",
)
data["time"] = list(zip(data.day, data.contact_time))

H = xgi.Hypergraph()
H["name"] = dataset_name

nodes1 = data["id1"].values.tolist()
nodes2 = data["id2"].values.tolist()
nodes = set()
nodes.update(set(nodes1))
nodes.update(set(nodes2))

H.add_nodes_from(nodes)

start_time = datetime(2019, 12, 22, 11, 31, 40)
# this is calculated by finding when the day switches and then subtracting
# the number of seconds elapsed at the switch. The data seems to start on
# Dec. 22 and end on Jan. 4

for t in data["time"].unique():
    days, sec = t
    time = timedelta(seconds=int(sec))
    d = data[data.time == t]
    links = d[["id1", "id2"]].values.tolist()
    G = nx.Graph(links)
    for e in nx.find_cliques(G):
        H.add_edge(e, timestamp=(start_time + time).isoformat())
    print(sec)


xgi.write_json(H, f"data/Malawi21/malawi-village.json")
