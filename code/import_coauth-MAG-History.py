import os

import utilities
import xgi

data_folder = "data"

dataset_name = "coauth-MAG-History-full"

new_dataset_name = "coauth-MAG-History"

dataset_folder = "coauth-MAG-History-full"
size_file = f"{dataset_name}-nverts.txt"
member_file = f"{dataset_name}-simplices.txt"
n_labels_file = f"{dataset_name}-node-labels.txt"
e_labels_file = f"{dataset_name}-simplex-labels.txt"
times_file = f"{dataset_name}-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
node_labels_file = os.path.join(data_folder, dataset_folder, n_labels_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)
H["name"] = new_dataset_name

delimiter = " "

node_labels = utilities.readScHoLPLabels(node_labels_file, delimiter)
edge_times = utilities.read_SCHOLP_dates(edge_times_file, time_unit="milliseconds")

H.add_nodes_from(list(node_labels.keys()))

for label, name in node_labels.items():
    H.nodes[label].update({"name": name})

for label, date in edge_times.items():
    H.edges[label].update({"timestamp": date})


xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{new_dataset_name}.json"))
