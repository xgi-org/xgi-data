import json
import os

import pandas as pd

data_folder = "data"

dataset_name = "eventernote-events"

new_dataset_name = "eventernote-events"

dataset_folder = "eventernote"
events_file = f"events.csv"
actors_file = f"actors.csv"
places_file = f"places.csv"
dest_file = f"{new_dataset_name}.json"

events_path = os.path.join(data_folder, dataset_folder, events_file)
actors_path = os.path.join(data_folder, dataset_folder, actors_file)
places_path = os.path.join(data_folder, dataset_folder, places_file)
dest_path = os.path.join(data_folder, dataset_folder, dest_file)

events = pd.read_csv(events_path)

# process events
# filter out events after 2024-04-30
events = events[events["event_date"] <= "2024-04-30"]
# drop events with no actors
events = events.dropna(subset=["actor_id"])
# drop duplicates
events.drop_duplicates(subset="id", inplace=True)
events.set_index("id", inplace=True)
events.sort_index(inplace=True)

# process actors

actors = pd.read_csv(actors_path)
actor_cols = ["id", "name", "kana", "initial", "sex"]
actors = actors[actor_cols]
# deduplicate actor ids
duplicates = actors[actors.duplicated(subset="id", keep=False)]
nan_ids = actors[actors["id"].isna()]
actors.drop_duplicates(subset="id", inplace=True)
actors.set_index("id", inplace=True)
actors.sort_index(inplace=True)
node_data = actors.to_dict(orient="index")

event_cols = ["event_date", "place_id", "event_name"]
events_save = events[event_cols].copy()
edge_data = events_save.to_dict(orient="index")


# nodes are actors
def process_actor_id(x):
    # if float or int, return as list
    if isinstance(x, (float, int)):
        return [str(x)]
    # if string, split and convert to list
    # return list(map(int, x.split(",")))
    return x.split(",")


edge_dict = events["actor_id"].map(process_actor_id).to_dict()

# corrections
# node 3065 in edge_dict[484] should be 3562
edge_dict[484].remove("3065")
edge_dict[484].append("3562")

# remove node 3668 from edge 116525
edge_dict[116525].remove("3668")

# add info for node 30071
node_data[30071] = {"name": "TOWA TEI", "kana": "ていとうわ", "initial": "て", "sex": 2}

# save

H = {"hypergraph-data": {"name": "eventernote-events"}}

H["node-data"] = node_data
H["edge-data"] = edge_data
H["edge-dict"] = edge_dict

with open(dest_path, "w") as f:
    json.dump(H, f)
