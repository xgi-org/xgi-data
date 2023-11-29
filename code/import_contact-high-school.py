import os
from datetime import datetime

import utilities
import xgi

data_folder = "data"

dataset_name = "contact-high-school"

dataset_folder = "contact-high-school"
size_file = "contact-high-school-nverts.txt"
member_file = "contact-high-school-simplices.txt"
times_file = "contact-high-school-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)
H["name"] = "contact-high-school"

edge_times = utilities.read_SCHOLP_dates(
    edge_times_file, reference_time=datetime(1970, 1, 1), time_unit="seconds"
)

for label, date in edge_times.items():
    H.edges[label].update({"timestamp": date})


xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{dataset_name}.json"))
