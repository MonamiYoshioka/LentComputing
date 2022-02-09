# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    
    
# Test created for Task 1F
def test_inconsistent_typical_range_stations():
    """Test created to see if the invalid_stations are the correct ones
        by looking at their typical_ranges values
    """
    # Build list of stations
    stations = build_station_list()
    # Build a list of stations iwht inconsistent typical range data
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    
    list_of_invalid_ranges = []
    for station in inconsistent_stations:
        list_of_invalid_ranges.append(station.typical_range)
    print(list_of_invalid_ranges)
    
test_inconsistent_typical_range_stations()