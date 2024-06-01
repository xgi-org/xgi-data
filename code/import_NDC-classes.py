import os
from datetime import datetime

import utilities

import xgi

data_folder = "data"

dataset_folder = "NDC-classes-full"
size_file = "NDC-classes-full-nverts.txt"
member_file = "NDC-classes-full-simplices.txt"
nlabels_file = "NDC-classes-full-node-labels.txt"
elabels_file = "NDC-classes-full-simplex-labels.txt"
times_file = "NDC-classes-full-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
node_labels_file = os.path.join(data_folder, dataset_folder, nlabels_file)
edge_labels_file = os.path.join(data_folder, dataset_folder, elabels_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)
H["name"] = "NDC-classes"

delimiter = " "

node_labels = utilities.readScHoLPLabels(node_labels_file, delimiter)
edge_labels = utilities.readScHoLPLabels(edge_labels_file, delimiter, two_column=False)

edge_times = utilities.read_SCHOLP_dates(
    edge_times_file, reference_time=datetime(1, 1, 1), time_unit="milliseconds"
)

H.add_nodes_from(list(node_labels.keys()))

H.set_edge_attributes(edge_labels, name="name")

for label, name in node_labels.items():
    H.nodes[label].update({"name": name})

for label, date in edge_times.items():
    H.edges[label].update({"timestamp": date})


xgi.write_json(H, os.path.join(data_folder, dataset_folder, "ndc-classes.json"))
