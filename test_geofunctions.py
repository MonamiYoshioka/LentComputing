from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


"""Test file for functions in geo.py"""

def test_stations_by_distance():

    stations = build_station_list()
    cambridge = (52.2053, 0.1218)
    check = stations_by_distance(stations,cambridge)
    print(check)
    assert check [0][2] > 0
    assert check [-1][2] < 1000 


def test_stations_within_radius():

    stations = build_station_list()
    cambridge = (52.2053, 0.1218)
    assert len(stations_within_radius(stations, (cambridge), 10)) == 11
    assert len(stations_within_radius(stations, (cambridge), 0)) == 0


def test_rivers_by_station_number():
    """Test to see whether the rivers_by_station_number funciton is running properly
    """
    
    stations = build_station_list()
    list1 = rivers_by_station_number(stations, 3)
    list2 = rivers_by_station_number(stations, 9)
    list3 = rivers_by_station_number(stations, 15)
    
    print(list2)
    
    assert len(list1) >= 3
    assert len(list2) >= 9
    assert len(list3) >= 15
    
    
test_rivers_by_station_number()