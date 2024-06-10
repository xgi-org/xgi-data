import matplotlib.pyplot as plt
import pandas as pd
import xgi

data_folder = "data"
collection_name = "hyperbard"

df = pd.read_csv(
    f"../{data_folder}/hyperbard_data/metadata/playtypes.csv", header=9, delimiter=","
)

play_type = df.set_index("play_name")["play_type"].to_dict()

collection = {}
for play in play_type:
    df = pd.read_csv(
        f"../{data_folder}/hyperbard_data/graphdata/{play}_hg-group-mw.edges.csv"
    )
    H = xgi.Hypergraph()

    for row in df["onstage"]:
        edge = set()
        for item in row.split(" "):
            edge.add(item.split("#")[1].split("_")[0])
        H.add_edge(edge)

    act = df["act"].to_dict()
    scene = df["scene"].to_dict()
    n_tokens = df["n_tokens"].to_dict()
    n_lines = df["n_lines"].to_dict()

    H.set_edge_attributes(act, name="act")
    H.set_edge_attributes(scene, name="scene")
    H.set_edge_attributes(n_tokens, name="n_tokens")
    H.set_edge_attributes(n_lines, name="n_lines")
    H["play-type"] = play_type[play]
    collection[play] = H

xgi.write_json_collection(
    collection,
    f"../{data_folder}/hyperbard_data/hyperbard",
    collection_name="hyperbard",
)
