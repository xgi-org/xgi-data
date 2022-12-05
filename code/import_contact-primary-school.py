import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import utilities
import xgi

output_stats = True
output_file = True

data_folder = "data"

dataset_folder = "contact-primary-school"
size_file = "contact-primary-school-nverts.txt"
member_file = "contact-primary-school-simplices.txt"
times_file = "contact-primary-school-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)
H["name"] = "contact-primary-school"

edge_times = utilities.read_SCHOLP_dates(
    edge_times_file, reference_time=datetime(1970, 1, 1), time_unit="seconds"
)

for label, date in edge_times.items():
    H.edges[label].update({"timestamp": date})

if output_stats:
    print((H.num_nodes, H.num_edges))

    print([len(c) for c in xgi.connected_components(H)])

    plt.figure(figsize=(8, 4))
    plt.subplot(121)

    degrees, counts = np.unique(H.nodes.degree.asnumpy(), return_counts=True)
    plt.loglog(degrees, counts / H.num_nodes, "ko", markersize=2)
    plt.title("Degree distribution")
    plt.xlabel(r"$k$", fontsize=16)
    plt.ylabel(r"$P(k)$", fontsize=16)
    plt.subplot(122)
    sizes, counts = np.unique(H.edges.size.asnumpy(), return_counts=True)
    plt.semilogy(sizes, counts / H.num_edges, "ko", markersize=2)
    plt.title("Edge size distribution")
    plt.xlabel(r"$m$", fontsize=16)
    plt.ylabel(r"$P(m)$", fontsize=16)
    plt.tight_layout()
    plt.savefig("data/contact-primary-school/stats.png", dpi=300)
    plt.show()


if output_file:
    xgi.write_json(
        H, os.path.join(data_folder, dataset_folder, "contact-primary-school.json")
    )
