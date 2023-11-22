import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import utilities
import xgi

output_stats = True
output_file = True

data_folder = "data"
datasheet_folder = "datasheets"

dataset_name = "congress-bills"

dataset_folder = "congress-bills"
size_file = "congress-bills-full-nverts.txt"
member_file = "congress-bills-full-simplices.txt"
labels_file = "congress-bills-full-node-labels.txt"
times_file = "congress-bills-full-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
node_labels_file = os.path.join(data_folder, dataset_folder, labels_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)
H["name"] = "congress-bills"

delimiter = "\t"

node_labels = utilities.readScHoLPLabels(node_labels_file, delimiter)
edge_times = utilities.read_SCHOLP_dates(edge_times_file)

H.add_nodes_from(list(node_labels.keys()))

for label, name in node_labels.items():
    H.nodes[label].update({"name": name})

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

    h = H.nodes.degree.ashist(density=True, log_binning=True)

    plt.loglog(h["bin_center"], h["value"], "ko", markersize=2)
    plt.title("Degree distribution")
    plt.xlabel(r"$k$", fontsize=16)
    plt.ylabel(r"$P(k)$", fontsize=16)
    plt.ylim([1e-5, 1])
    sns.despine()

    plt.subplot(122)
    h = H.edges.size.ashist(density=True, log_binning=True)
    plt.loglog(h["bin_center"], h["value"], "ko", markersize=2)
    plt.title("Edge size distribution")
    plt.xlabel(r"$s$", fontsize=16)
    plt.ylabel(r"$P(s)$", fontsize=16)
    plt.ylim([1e-5, 1])
    sns.despine()
    plt.tight_layout()
    plt.savefig(f"{datasheet_folder}/{dataset_name}/stats.png", dpi=300)
    plt.show()


if output_file:
    xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{dataset_name}.json"))
