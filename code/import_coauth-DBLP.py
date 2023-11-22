import os

import matplotlib.pyplot as plt
import numpy as np
import utilities
import xgi

output_stats = True
output_file = True

data_folder = "data"

dataset_name = "coauth-DBLP-full"
dataset_folder = f"{dataset_name}"
size_file = f"{dataset_name}-nverts.txt"
member_file = f"{dataset_name}-simplices.txt"
n_labels_file = f"{dataset_name}-node-labels.txt"
times_file = f"{dataset_name}-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
node_labels_file = os.path.join(data_folder, dataset_folder, n_labels_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)
H["name"] = "coauth-DBLP"

delimiter = " "

node_labels = utilities.readScHoLPLabels(node_labels_file, delimiter)
edge_times = utilities.read_SCHOLP_dates(edge_times_file, time_unit="years")

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

    degrees, counts = np.unique(H.nodes.degree.asnumpy(), return_counts=True)
    plt.loglog(degrees, counts / H.num_nodes, "ko", markersize=2)
    plt.title("Degree distribution")
    plt.xlabel(r"$k$", fontsize=16)
    plt.ylabel(r"$P(k)$", fontsize=16)
    plt.subplot(122)
    sizes, counts = np.unique(H.edges.size.asnumpy(), return_counts=True)
    plt.plot(sizes, counts / H.num_edges, "ko", markersize=2)
    plt.title("Edge size distribution")
    plt.xlabel(r"$m$", fontsize=16)
    plt.ylabel(r"$P(m)$", fontsize=16)
    plt.tight_layout()
    plt.savefig(f"{data_folder}/{dataset_folder}/stats.png", dpi=300)
    plt.show()


if output_file:
    xgi.write_json(H, os.path.join(data_folder, dataset_folder, f"{dataset_name}.json"))