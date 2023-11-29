import os
import xml.etree.ElementTree as ET

import xgi

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
                        if (
                            attr.attrib["id"] == "0"
                            and attr.attrib["value"] == "disease"
                        ):
                            node_attr[node.attrib["id"]] = {
                                "label": node.attrib["label"]
                            }
                        elif (
                            attr.attrib["id"] == "0" and attr.attrib["value"] == "gene"
                        ):
                            edge_attr[node.attrib["id"]] = {
                                "label": node.attrib["label"]
                            }

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


xgi.write_json(H, os.path.join(data_folder, dataset_folder, "diseasome.json"))
