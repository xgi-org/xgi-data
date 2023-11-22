import os

import xgi

data_folder = "data"

dataset_name = "cat-edge-Cooking"
new_dataset_name = "kaggle-whats-cooking"

dataset_folder = f"{dataset_name}"
edges_file = "hyperedges.txt"
n_labels_file = "node-labels.txt"
e_labels_file = "hyperedge-labels.txt"
l_identities_file = "hyperedge-label-identities.txt"

edgelist_file = os.path.join(data_folder, dataset_folder, edges_file)
node_labels_file = os.path.join(data_folder, dataset_folder, n_labels_file)
edge_labels_file = os.path.join(data_folder, dataset_folder, e_labels_file)
label_identities_file = os.path.join(data_folder, dataset_folder, l_identities_file)

H = xgi.read_edgelist(edgelist_file, delimiter="\t", nodetype=int)
H["name"] = new_dataset_name

with open(node_labels_file) as f:
    node_labels = f.read().splitlines()

for i, n in enumerate(H.nodes):
    H.nodes[n].update({"name": node_labels[i]})

with open(edge_labels_file) as f:
    edge_labels = f.read().splitlines()

with open(label_identities_file) as f:
    edge_label_identities = f.read().splitlines()

for i, e in enumerate(H.edges):
    H.edges[e].update({"name": edge_label_identities[int(edge_labels[i]) - 1]})


xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{new_dataset_name}.json"))
