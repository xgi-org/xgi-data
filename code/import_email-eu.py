import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import utilities
import xgi

output_stats = True
output_file = False

preexisting = True

data_folder = "data"
datasheet_folder = "datasheets"

if preexisting:
    H = xgi.load_xgi_data("email-eu")
    dataset_name = H["name"]
else:
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

if output_stats:
    print((H.num_nodes, H.num_edges))

    vals, counts = np.unique(
        [len(c) for c in xgi.connected_components(H)], return_counts=True
    )
    print(np.array([vals, counts]))

    plt.figure(figsize=(8, 4))
    plt.subplot(121)

    h = H.nodes.degree.ashist(bins=20, density=True, log_binning=True)

    plt.loglog(h["bin_center"], h["value"], "ko", markersize=2)
    plt.title("Degree distribution")
    plt.xlabel(r"$k$", fontsize=16)
    plt.ylabel(r"$P(k)$", fontsize=16)
    # plt.ylim([1e-5, 1])
    sns.despine()

    plt.subplot(122)
    h = H.edges.size.ashist(bins=12, density=True)
    plt.semilogy(h["bin_center"], h["value"], "ko", markersize=2)
    plt.title("Edge size distribution")
    plt.xlabel(r"$s$", fontsize=16)
    plt.ylabel(r"$P(s)$", fontsize=16)
    # plt.ylim([1e-5, 1])
    sns.despine()
    plt.tight_layout()
    plt.savefig(f"{datasheet_folder}/{dataset_name}/stats.png", dpi=300)
    plt.show()


if output_file:
    xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{dataset_name}.json"))
