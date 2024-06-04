import os
from datetime import datetime, timedelta

import networkx as nx
import pandas as pd

import xgi

dataset_name = "Science-Gallery"

start_time = datetime(1970, 1, 1)
H = xgi.Hypergraph()
H["name"] = dataset_name

for fname in sorted(os.listdir("data/ScienceGallery")):
    if "listcontacts" in fname:
        data = pd.read_csv(
            "data/ScienceGallery/" + fname,
            sep="\t",
            header=0,
            names=["time", "node1", "node2"],
        )

        nodes1 = data["node1"].values.tolist()
        nodes2 = data["node2"].values.tolist()
        nodes = set()
        nodes.update(set(nodes1))
        nodes.update(set(nodes2))

        H.add_nodes_from(nodes)

        for t in data["time"].unique():
            time = timedelta(seconds=int(t))
            d = data[data.time == t]
            links = d[["node1", "node2"]].values.tolist()
            G = nx.Graph(links)
            for e in nx.find_cliques(G):
                H.add_edge(e, timestamp=(start_time + time).isoformat())
        print(f"{fname} completed!")


xgi.write_json(H, f"data/ScienceGallery/science-gallery.json")
