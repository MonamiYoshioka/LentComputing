from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    # Build list of stations
    stations = build_station_list()
    
     # Get set of rivers which have a monitoring station
    river_set = rivers_with_station(stations)
     # Print number of rivers with at least 1 station
    print("{} stations".format(len(river_set)))
    # Print first 10 of these rivers
    print("First 10 stations: ", sorted(river_set)[:10])
    
    # Get dictionary of rivers as keys with a list of station objects
    river_station_dic = stations_by_river(stations)
    
    # List the stations in these rivers in alphabetical order
    list_rivers = ['River Aire', 'River Cam', 'River Thames']
    for river in list_rivers:
        list_stations = river_station_dic[river]
        print("{} has stations: {}\n".format(river, sorted(list_stations)))
    
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()