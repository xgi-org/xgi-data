import os

import utilities
import xgi

delimiter = " "

data_folder = "data"

dataset_name = "threads-math-sx"
dataset_folder = f"{dataset_name}"
size_file = f"{dataset_name}-nverts.txt"
member_file = f"{dataset_name}-simplices.txt"
e_labels_file = f"{dataset_name}-simplex-labels.txt"
times_file = f"{dataset_name}-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
edge_labels_file = os.path.join(data_folder, dataset_folder, e_labels_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

edge_labels = utilities.readScHoLPLabels(edge_labels_file, delimiter, two_column=False)
H = xgi.Hypergraph(dict(zip(edge_labels, edgelist)))
H["name"] = dataset_name

edge_times = utilities.read_SCHOLP_dates(edge_times_file, time_unit="milliseconds")

for label, date in edge_times.items():
    H.edges[label].update({"timestamp": date})


xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{dataset_name}.json"))
