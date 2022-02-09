from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    # Build list of stations
    stations = build_station_list()
    
    # Build a list of stations iwht inconsistent typical range data
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    
    # Make a list of names of these inconsistent stations, then sort list and print it
    final_list = []
    for station in inconsistent_stations:
        final_list.append(station.name)
    print(sorted(final_list))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
    
