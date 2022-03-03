from random_data import get_madeup_station_list
import floodsystem.flood

def test_stations_level_over_threshold():
    stations = get_madeup_station_list()
    tol = 1
    station_threshold = floodsystem.flood.stations_level_over_threshold(stations, tol)
    
    print(station_threshold)
    assert station_threshold[0][1] == 4.0
    assert station_threshold[1][1] == 3.0
    assert station_threshold[2][1] == 2.0
    
def test_stations_highest_rel_level():
    stations = get_madeup_station_list()
    N = 2
    max_stations = floodsystem.flood.stations_highest_rel_level(stations, N)
    
    assert len(max_stations) == 2
    assert max_stations[0][1] > 1
    assert max_stations[1][1] > 1