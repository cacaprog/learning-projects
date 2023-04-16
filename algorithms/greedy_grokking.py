# Set to build an unordered collection of unique elements
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()


def my_set_covering(states_needed, stations):
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station  # intersection
            if len(covered) > len(states_covered) and station not in final_stations:
                best_station = station
                states_covered = covered
        if best_station is not None:
            states_needed -= states_covered
            final_stations.add(best_station)
            stations.pop(best_station)
        else:
            return None
    return final_stations


print(my_set_covering(states_needed, stations))
