# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


# Task 1D
def rivers_with_station(stations):
    """Find rivers which have monitoring stations

    Args:
        stations (list): list of MonitoringStation objects

    Returns:
        set: contains name of the rivers with a monitoring station
    """
    river_set = set()
    for station in stations:
        river_set.add(station.river)
    return river_set
    

def stations_by_river(stations):
    """Find stations which are by the same river

    Args:
        stations (list): list of MonitoringStation objects
        
    Returns:
        dictionary: river name as key to a list of station names
    """
    dic_stations_river = {}
    for station in stations:
        key = station.river
        if key in dic_stations_river:
            dic_stations_river[key].append(station.name)
        else:
            dic_stations_river[key] = [station.name]
        
    return dic_stations_river


# Task 1E
def rivers_by_station_number(stations, N):
    """Determine N rivers with greatest number of stations

    Args:
        stations (list): list of MonitoringStation objects
        N (int): number of stations
    Return:
        list: sorted list of (river name, number of stations) tuple
    """
    
    