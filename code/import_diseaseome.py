import xgi
import xml.etree.ElementTree as ET
import os
import matplotlib.pyplot as plt
import numpy as np

output_stats = True
output_file = True

data_folder = "data"

dataset_folder = "diseasome"

H = xgi.Hypergraph()
tree = ET.parse(os.path.join(data_folder, dataset_folder, "diseasome.gexf"))
root = tree.getroot()

node_attr = dict()
edge_attr = dict()
for item in root:
    for subelement in item:
        if "nodes" in subelement.tag:
            for node in subelement:
                for attrlist in node:
                    for attr in attrlist:
                        if attr.attrib["id"] == "0" and attr.attrib["value"] == "disease":
                            node_attr[node.attrib["id"]] = {"label":node.attrib["label"]}
                        elif attr.attrib["id"] == "0" and attr.attrib["value"] == "gene":
                            edge_attr[node.attrib["id"]] = {"label":node.attrib["label"]}

for item in root:
    for subelement in item:
        if "edges" in subelement.tag:
                for edge in subelement:
                    source = edge.attrib["source"]
                    target = edge.attrib["target"]
                    if source in node_attr and target in edge_attr:
                        H.add_node_to_edge(edge.attrib["target"], edge.attrib["source"])
                    elif target in node_attr and source in edge_attr:
                        H.add_node_to_edge(edge.attrib["source"], edge.attrib["target"])
                    else:
                        print(f"Edge ({source}, {target}) Not bipartite!")

xgi.set_edge_attributes(H, edge_attr)
xgi.set_node_attributes(H, node_attr)
H["name"] = "Diseasome"


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
    plt.loglog(sizes, counts / H.num_edges, "ko", markersize=2)
    plt.title("Edge size distribution")
    plt.xlabel(r"$m$", fontsize=16)
    plt.ylabel(r"$P(m)$", fontsize=16)
    plt.tight_layout()
    plt.savefig("data/diseasome/stats.png", dpi=300)
    plt.show()


if output_file:
    xgi.write_json(H, os.path.join(data_folder, dataset_folder, "diseasome.json"))