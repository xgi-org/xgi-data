import os

import utilities
import xgi

data_folder = "data"

dataset_folder = "NDC-substances"
size_file = "NDC-substances-nverts.txt"
member_file = "NDC-substances-simplices.txt"
labels_file = "NDC-substances-node-labels.txt"
times_file = "NDC-substances-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
node_labels_file = os.path.join(data_folder, dataset_folder, labels_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)
H["name"] = "NDC-substances"

delimiter = " "

node_labels = utilities.readScHoLPLabels(node_labels_file, delimiter)

H.add_nodes_from(list(node_labels.keys()))

for label, name in node_labels.items():
    H.nodes[label].update({"name": name})


xgi.write_json(H, os.path.join(data_folder, dataset_folder, "NDC-substances.json"))
