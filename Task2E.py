import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()
    
    # Get N stations with the greatest water levels
    N = 5
    update_water_levels(stations)
    N_stations = stations_highest_rel_level(stations, N)
    
    # Plot the water level data against time (past dt days) for each station in N_stations
    dt = 10
    for station in stations:
        if station.name in (i[0] for i in N_stations):
            dates, level = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_level(station, dates, level)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
