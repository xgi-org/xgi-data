import json
import os

import pandas as pd

data_folder = "data"

dataset_name = "eventernote-places"

new_dataset_name = "eventernote-places"

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
events = events.dropna(subset=["actor_id", "place_id"])
events["place_id"] = events["place_id"].astype(int)
# drop duplicates
events.drop_duplicates(subset="id", inplace=True)
# drop NAs in place ids
events.set_index("id", inplace=True)
events.sort_index(inplace=True)

# process places
places = pd.read_csv(places_path)
places_cols = ["id", "place_name", "prefecture"]
places = places[places_cols]
# deduplicate place ids
places.drop_duplicates(subset="id", inplace=True)
places.set_index("id", inplace=True)
places.sort_index(inplace=True)
edge_data = places.to_dict(orient="index")

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


# nodes are actors
def process_actor_id(x):
    # if float or int, return as list
    if isinstance(x, (float, int)):
        return [str(x)]
    # if string, split and convert to list
    # return list(map(int, x.split(",")))
    return x.split(",")


# for every event, add actor_ids to the place id
edge_dict = {int(x): [] for x in edge_data.keys()}
edge_dict[974] = []
edge_dict[0] = []
for idx, row in events.iterrows():
    actor_ids = process_actor_id(row["actor_id"])
    for actor_id in actor_ids:
        edge_dict[int(row["place_id"])].append(actor_id)

# remove empty edges
edge_dict = {k: v for k, v in edge_dict.items() if v}

# corrections
# node 3065 in edge_dict[43] should be 3562
edge_dict[43].remove("3065")
edge_dict[43].append("3562")

# remove node 3668 from edge 3080
edge_dict[3080].remove("3668")

# add info for node 30071
node_data[30071] = {"name": "TOWA TEI", "kana": "ていとうわ", "initial": "て", "sex": 2}

# add info for edges 974 and 0
edge_data[974] = {"place_name": "未定", "prefecture": "0"}

edge_data[0] = {"place_name": "未定", "prefecture": "0"}

# save

H = {
    "hypergraph-data": {
        "name": new_dataset_name,
    }
}

H["node-data"] = node_data
H["edge-data"] = edge_data
H["edge-dict"] = edge_dict

with open(dest_path, "w") as f:
    json.dump(H, f)
