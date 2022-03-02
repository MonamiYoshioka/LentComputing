# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    # Created in Task 1F
    def typical_range_consistent(self):
        """Checks typical high/low range data for consistecy
        
        Return:
            bool: True if data is consistent, False if inconsistent or unavailable
        """
        
        try:
            # Compare the first and last values in the typical_range tuple
            # If the second value is higher than the first, then data is consistent
            if self.typical_range[0] < self.typical_range[1]: return True
            else: return False
        except:
            # No data available for the typical_range, omit station
            return False

            

    #created for Task 2B
    def relative_water_level(self):
        """returns latest water level as a fraction of the typical range"""

        if type(self.latest_level) != float or self.typical_range is None:
            return None
        else:
            
            range = self.typical_range[1] - self.typical_range[0]
            return (self.latest_level - self.typical_range[0])/range


    
# Created in Task 1F
def inconsistent_typical_range_stations(stations):
    """Find stations which have inconsistent data
    
    Args:
        stations (list): list of MonitoringStation objects
    Return:
        list: stations that have inconsistent data
    """
    
    inconsistent_stations = []
    for station in stations:
        is_data_consistent = station.typical_range_consistent()
        if is_data_consistent != True:
            inconsistent_stations.append(station)
    
    return inconsistent_stations

def consistent_typical_range_stations(stations):
    """Find stations which have consistent data
    
    Args:
        stations (list): list of MonitoringStation objects
    Return:
        list: stations that have consistent data
    """
    consistent_stations = []
    for station in stations:
        is_data_consistent = station.typical_range_consistent()
        if is_data_consistent == True:
            consistent_stations.append(station)
    
    return consistent_stations
    