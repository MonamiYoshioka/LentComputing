"""Task is to list the towns where I assess 
    the risk of flooding to be the greatest
    
    Criteria used to make the assessment:
    'Severe' - the current relative water level is 50% higher than the typical high AND the water level at the station is rising
    'High' - the latest water level is higher than the typical high but water level is not risinf
    'Moderate' - the water level at the station is rising but water level is not above typical high
    'Low' - the latest water level is not higher than the typical high and the water level at the station is not rising
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import create_flood_risk_list
from floodsystem.station import MonitoringStation
from floodsystem.utils import print_risk

def run():
    # Make list of stations, and get their water level values
    stations = build_station_list()
    update_water_levels(stations)
    
    # Set the thershold, if stations current relative level is over tolerance, then its at a high risk of flooding
    tol = 1.5
    gradient_thresh = 0.1
    
    severe, high, moderate, low = create_flood_risk_list(stations, tol, gradient_thresh)
        
    print_risk(severe, "SEVERE")
    print_risk(high, "HIGH")
    print_risk(moderate, "MODERATE")
    print_risk(low, "LOW")


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()