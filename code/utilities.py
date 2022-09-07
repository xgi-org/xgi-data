import json
from datetime import datetime, timedelta


def readScHoLPData(edge_size_file, member_ID_file):
    edgelist = list()
    with open(edge_size_file) as size_file, open(member_ID_file) as id_file:
        sizes = size_file.read().splitlines()
        members = id_file.read().splitlines()
        member_index = 0
        for index in range(len(sizes)):
            edge = list()
            edge_size = int(sizes[index])
            for i in range(member_index, member_index + edge_size):
                member = members[i]
                edge.append(member)
            edgelist.append(tuple(edge))
            member_index += edge_size
    return edgelist


def readScHoLPNodeLabels(node_labels_file, delimiter):
    label_dict = dict()
    with open(node_labels_file) as label_data:
        for line in label_data:
            s = line.split(delimiter, 1)
            label_dict[s[0]] = s[1].rstrip("\n")
    return label_dict


def read_SCHOLP_dates(
    timestamp_file, reference_time=datetime(1, 1, 1), time_unit="days"
):

    time_dict = dict()
    with open(timestamp_file) as time_data:
        lines = time_data.read().splitlines()
        for i in range(len(lines)):
            if time_unit == "days":
                time = reference_time + timedelta(days=int(lines[i]))
            elif time_unit == "seconds":
                time = reference_time + timedelta(seconds=int(lines[i]))
            elif time_unit == "milliseconds":
                time = reference_time + timedelta(seconds=int(lines[i]) / 1000)
            time_dict[i] = time.isoformat()
    return time_dict
