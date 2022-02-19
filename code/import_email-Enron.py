import matplotlib.pyplot as plt
import utilities
import os
import xgi
import numpy as np

output_stats = True
output_file = False

data_folder = "Data"

dataset_folder = "email-Enron"
size_file = "email-Enron-full-nverts.txt"
member_file = "email-Enron-full-simplices.txt"
labels_file = "email-Enron-full-node-labels.txt"
times_file = "email-Enron-full-times.txt"

hyperedge_size_file = os.path.join(data_folder, dataset_folder, size_file)
member_ID_file = os.path.join(data_folder, dataset_folder, member_file)
node_labels_file = os.path.join(data_folder, dataset_folder, labels_file)
edge_times_file = os.path.join(data_folder, dataset_folder, times_file)

edgelist = utilities.readScHoLPData(hyperedge_size_file, member_ID_file)

H = xgi.Hypergraph(edgelist)

delimiter = " "

node_labels = utilities.readScHoLPNodeLabels(node_labels_file, delimiter)
edge_times = utilities.read_SCHOLP_dates(edge_times_file, time_unit="milliseconds")

H.add_nodes_from(list(node_labels.keys()))

for label, name in node_labels.items():
    H.nodes[label].update({"name": name})

for label, date in edge_times.items():
    H.edges[label].update({"timestamp": date})

if output_stats:
    print(H.shape)

    plt.figure(figsize=(8, 4))
    plt.subplot(121)

    degrees, counts = np.unique([H.degree(n) for n in H.nodes], return_counts=True)
    plt.loglog(degrees, counts / H.number_of_nodes(), "ko", markersize=2)
    plt.title("Degree distribution")
    plt.xlabel(r"$k$", fontsize=16)
    plt.ylabel(r"$P(k)$", fontsize=16)
    plt.subplot(122)
    sizes, counts = np.unique([H.edge_size(e) for e in H.edges], return_counts=True)
    plt.loglog(sizes, counts / H.number_of_edges(), "ko", markersize=2)
    plt.title("Edge size distribution")
    plt.xlabel(r"$m$", fontsize=16)
    plt.ylabel(r"$P(m)$", fontsize=16)
    plt.tight_layout()
    plt.savefig("data/email-Enron/stats.png", dpi=300)
    plt.show()


if output_file:
    utilities.write_hypergraph_json(
        H, os.path.join(data_folder, dataset_folder, "email-Enron.json")
    )
