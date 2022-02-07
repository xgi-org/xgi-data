from ctypes import util
from platform import node
import utilities
import os
import xgi

data_folder = "Data"

dataset_folder = "email-Enron"
size_file = "email-Enron-nverts.txt"
member_file = "email-Enron-simplices.txt"
labels_file = "email-Enron-node-labels.txt"
times_file = "email-Enron-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
node_labels_file = os.path.join(data_folder, dataset_folder, labels_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)

delimiter = " "

node_labels = utilities.readScHoLPNodeLabels(node_labels_file, delimiter)
edge_times = utilities.read_SCHOLP_dates(edge_times_file, time_unit="seconds")

H.add_nodes_from(list(node_labels.keys()))

for label, name in node_labels.items():
    H.nodes[label].update({"email": name})

for label, date in edge_times.items():
    H.edges[label].update({"date": date})

utilities.write_hypergraph_json(H, os.path.join(data_folder, dataset_folder, "email-Enron.json"))