# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key, get_N_max_integers  # noqa
from haversine import haversine 

# Task 1B
def stations_by_distance(stations, p):
    """this function creates a sorted list of stations and their distances from a coordinate,p
    
    Args:
        stations(list): list of MonitoringStation class objects
        p(tuple): tuple of coordinates (longitude, latitude)

    Returns:
        list: a list of tuples sorted by decending distance from coordinate p
    """
    distance_list = []
    for each in stations:
        coord = each.coord
        distance = haversine(p, coord)
        temp_tuple = (each.name, each.town, distance)
        distance_list.append(temp_tuple)
    distance_list = sorted_by_key(distance_list, 1)
    return distance_list

# Task 1C
def stations_within_radius(stations, centre, r):
    """prints an alphabetic list of the stations withink a radius, r, around a centre"""
    radius_list = []
    for each in stations:
        coord = each.coord
        radius = haversine(coord,centre)
        
        if radius<r:
            radius_list.append(each.name)

    radius_list = sorted(radius_list)
    return radius_list



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
        N (int): max number of station numbers
    Return:
        list: sorted list of (river name, number of stations) tuple
    """
    
    # Create a dictionary of rivers as keys
    river_number_stations = {}
    for station in stations:
        if station.river in river_number_stations:
            river_number_stations[station.river] += 1
        else:
            river_number_stations[station.river] = 1
    
    # Sort dictionary values in ascending order:
    river_number_stations = dict(sorted(river_number_stations.items(), key=lambda x:x[1], reverse=True))
    
    # Function to get N max integers of the dictionary values without duplicates
    numbers = get_N_max_integers(river_number_stations, N)
    
    # Find rivers with 'numbers' amount of stations and create a list with them
    # List of tuples -> (river name, numnber of stations)
    final_list = []
    [final_list.append((key, value)) for key, value in river_number_stations.items() if value in numbers]
    return final_list