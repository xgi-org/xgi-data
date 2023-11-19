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


def readScHoLPLabels(labels_file, delimiter="\t", two_column=True):
    label_dict = dict()
    with open(labels_file) as label_data:
        for i, line in enumerate(label_data):
            if two_column:
                s = line.split(delimiter, 1)
                idx = s[0]
                val = s[1].rstrip("\n")
            else:
                idx = i
                val = line.rstrip("\n")
            label_dict[idx] = val
    return label_dict


def read_SCHOLP_dates(
    timestamp_file, reference_time=datetime(1, 1, 1), time_unit="days"
):
    time_dict = dict()
    with open(timestamp_file) as time_data:
        lines = time_data.read().splitlines()
        for i in range(len(lines)):
            t = int(lines[i])
            if time_unit == "days":
                time = reference_time + timedelta(days=t)
            elif time_unit == "seconds":
                time = reference_time + timedelta(seconds=t)
            elif time_unit == "milliseconds":
                time = reference_time + timedelta(seconds=t / 1000)
            elif time_unit == "quarters":
                year = int((t - 1) / 4)
                quarter = (t - 1) % 4 + 1
                time = datetime(year, int(3 * quarter), 1)
            elif time_unit == "years":
                year = t
                time = datetime(year, 1, 1)
            time_dict[i] = time.isoformat()
    return time_dict
