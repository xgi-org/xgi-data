import os

import utilities
import xgi

delimiter = " "

data_folder = "data"

dataset_folder = "threads-ask-ubuntu"
size_file = "threads-ask-ubuntu-nverts.txt"
member_file = "threads-ask-ubuntu-simplices.txt"
e_labels_file = "threads-ask-ubuntu-simplex-labels.txt"
times_file = "threads-ask-ubuntu-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
edge_label_file = os.path.join(data_folder, dataset_folder, e_labels_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)
edge_labels = utilities.readScHoLPLabels(edge_label_file, delimiter, two_column=False)

H = xgi.Hypergraph(dict(zip(edge_labels, edgelist)))
H["name"] = "threads-ask-ubuntu"


edge_times = utilities.read_SCHOLP_dates(edge_times_file, time_unit="milliseconds")

for label, date in edge_times.items():
    H.edges[label].update({"timestamp": date})

xgi.write_json(H, os.path.join(data_folder, dataset_folder, "threads-ask-ubuntu.json"))
