import os
from datetime import datetime

import utilities

import xgi

data_folder = "data"

dataset_name = "contact-primary-school"

dataset_folder = "contact-primary-school"
size_file = "contact-primary-school-nverts.txt"
member_file = "contact-primary-school-simplices.txt"
times_file = "contact-primary-school-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)
H["name"] = dataset_name

edge_times = utilities.read_SCHOLP_dates(
    edge_times_file, reference_time=datetime(1970, 1, 1), time_unit="seconds"
)

for label, date in edge_times.items():
    H.edges[label].update({"timestamp": date})


xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{dataset_name}.json"))
