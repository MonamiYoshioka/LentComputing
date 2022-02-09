from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


"""Test file for functions in geo.py"""


def test_rivers_by_station_number():
    """Test to see wether the rivers_by_station_number funciton is running properly
    """
    
    stations = build_station_list()
    list1 = rivers_by_station_number(stations, 3)
    list2 = rivers_by_station_number(stations, 9)
    list3 = rivers_by_station_number(stations, 15)
    
    print(list2)
    
    assert len(list1) >= 3
    assert len(list2) >= 9
    assert len(list3) >= 15