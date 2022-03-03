"""Task is to list the towns where I assess 
    the risk of flooding to be the greatest
    
    Criteria used to make the assessment:
    'Severe' - the current relative water level is 50% higher than the typical high AND the water level at the station is rising
    'High' - the latest water level is higher than the typical high AND the water level at the station is rising AND water level is above typical low
    'Moderate' - the latest water level is higher than the typical high OR the water level at the station is rising AND water level is below typical low
    'Low' - the latest water level is not higher than the typical high and the water level at the station is not rising
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import gradient_analysis
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.station import MonitoringStation

def run():
    # Make list of stations, and get their water level values
    stations = build_station_list()
    update_water_levels(stations)
    
    # Set the thershold, if stations current relative level is over tolerance, then its at a high risk of flooding
    tol = 1.5
    gradient_thresh = 0.1
    
    station_relative_level_over_1 = []
    station_severe_risk = []
    station_threshold = stations_level_over_threshold(stations, tol)
    for station in station_threshold:
        station_relative_level_over_1.append(station)
    
    # Check wether the polyfit gradient is above or below zero
    # If above zero, water level is rising
     # Plot the water level data against time (past dt days) for each station in N_stations
    dt = 2
    for station in stations:
        if station.name in (i[0] for i in station_relative_level_over_1):
            dates, level = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            try:
                gradient = gradient_analysis(dates, level, 4)
                if gradient > gradient_thresh:
                    station_severe_risk.append(station)
                    station.gradient = gradient
            except:
                print(f"Valid data not available for {station.name}")
    
    
    print(f"----------------------------------------------------------\n")
    print(f"List of stations at a SEVERE risk of flooding:\n")
    print(f"----------------------------------------------------------\n")
    for station in station_severe_risk:
        print(f"Name: {station.name}")
        print(f"Current relative water level: {MonitoringStation.relative_water_level(station)}")
        print(f"Water level rising at a rate of: {station.gradient} \n")


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()