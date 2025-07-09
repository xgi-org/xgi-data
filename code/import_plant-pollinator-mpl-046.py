import os

import numpy as np
import pandas as pd
import utilities
import xgi

data_folder = "data/"
dataset_name = "plant-pollinator-mpl-046"
dataset_folder = f"{data_folder}{dataset_name}/"

incidence_file = f"{dataset_folder}/M_PL_046.csv"

incidence_matrix_df = pd.read_csv(incidence_file, index_col=0)

plants = list(incidence_matrix_df.index)
pollinators = list(incidence_matrix_df.columns)

H = xgi.Hypergraph(incidence_matrix_df.values)

plant_dict = {i: species for i, species in enumerate(plants)}

pollinator_dict = {i: species for i, species in enumerate(pollinators)}

H.set_node_attributes(plant_dict, name="plant")
H.set_edge_attributes(pollinator_dict, name="pollinator")

H["name"] = dataset_name

xgi.write_json(H, f"{dataset_folder}{dataset_name}.json")
