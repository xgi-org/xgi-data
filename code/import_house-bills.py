import os

import utilities
import xgi

data_folder = "data"

dataset_name = "house-bills"

new_dataset_name = "house-bills"

dataset_folder = "house-bills"
edgelist_file = f"hyperedges-{dataset_name}.txt"
node_names_file = f"node-names-{dataset_name}.txt"
node_affiliations_file = f"node-labels-{dataset_name}.txt"
affiliation_names_file = f"label-names-{dataset_name}.txt"

edgelist_filepath = os.path.join(data_folder, dataset_folder, edgelist_file)
node_names_filepath = os.path.join(data_folder, dataset_folder, node_names_file)
node_affiliations_filepath = os.path.join(
    data_folder, dataset_folder, node_affiliations_file
)
affiliation_names_filepath = os.path.join(
    data_folder, dataset_folder, affiliation_names_file
)

H = xgi.read_edgelist(edgelist_filepath, delimiter=",")
H["name"] = new_dataset_name

node_labels = utilities.readScHoLPLabels(node_names_filepath, two_column=False)
node_affiliation = utilities.readScHoLPLabels(
    node_affiliations_filepath, two_column=False
)

for id, name in node_labels.items():
    H.nodes[str(id)].update({"name": name})

affiliation_names = []
with open(affiliation_names_filepath) as label_data:
    for line in label_data:
        affiliation_names.append(line.strip("\n"))

for id, label in node_affiliation.items():
    H.nodes[str(id)].update({"affiliation": affiliation_names[int(label) - 1]})

xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{new_dataset_name}.json"))
