import os
from datetime import datetime

import utilities

import xgi

data_folder = "data"

dataset_name = "email-Eu"

dataset_folder = "email-Eu"
size_file = "email-Eu-full-nverts.txt"
member_file = "email-Eu-full-simplices.txt"
times_file = "email-Eu-full-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)
H["name"] = dataset_name

delimiter = "\t"

edge_times = utilities.read_SCHOLP_dates(
    edge_times_file, reference_time=datetime(1970, 1, 1), time_unit="seconds"
)

for label, date in edge_times.items():
    H.edges[label].update({"timestamp": date})


xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{dataset_name}.json"))
