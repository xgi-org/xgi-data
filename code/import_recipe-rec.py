import json
import xgi

data_folder = "data"
dataset_name = "recipe-rec"
filename = "recipes_weighted_and_USDAmapped.json"
new_dataset_name = "recipe-rec"

with open(f"{data_folder}/{dataset_name}/{filename}") as file:
        jsondata = json.loads(file.read())

H = xgi.Hypergraph()
for entry in jsondata:
    e = set()
    for item in entry["ingredients"]:
        e.add(item["text"])
    H.add_edge(e, id=entry["id"], name=entry["title"], url=entry["url"])

H["name"] = "recipe-rec"

xgi.write_hif(H, f"{data_folder}/{dataset_name}/{new_dataset_name}.json")