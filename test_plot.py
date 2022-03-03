from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_gradient
import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels

def test_plot_gradient():
    # Make list of stations, and get their water level values
    stations = build_station_list()
    update_water_levels(stations)
    
    # Get N stations with the greatest water levels
    N = 5
    update_water_levels(stations)
    N_stations = stations_highest_rel_level(stations, N)
    
    # Plot the water level data against time (past dt days) for each station in N_stations
    dt = 2
    for station in stations:
        if station.name in (i[0] for i in N_stations):
            dates, level = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            try:
                plot_gradient(station, dates, level, 4)
            except:
                print(f"Valid data not available for {station.name}")

test_plot_gradient()