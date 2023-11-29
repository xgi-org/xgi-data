import os

import utilities
import xgi

data_folder = "data"

dataset_name = "congress-bills"

dataset_folder = "congress-bills"
size_file = "congress-bills-full-nverts.txt"
member_file = "congress-bills-full-simplices.txt"
labels_file = "congress-bills-full-node-labels.txt"
times_file = "congress-bills-full-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
node_labels_file = os.path.join(data_folder, dataset_folder, labels_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)
H["name"] = "congress-bills"

delimiter = "\t"

node_labels = utilities.readScHoLPLabels(node_labels_file, delimiter)
edge_times = utilities.read_SCHOLP_dates(edge_times_file)

H.add_nodes_from(list(node_labels.keys()))

for label, name in node_labels.items():
    H.nodes[label].update({"name": name})

for label, date in edge_times.items():
    H.edges[label].update({"timestamp": date})


xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{dataset_name}.json"))
