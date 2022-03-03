from floodsystem.station import MonitoringStation
from floodsystem.station import consistent_typical_range_stations


def stations_level_over_threshold(stations, tol):
    """Find all stations with valid data which have a latest
    relative water level over the tolerance

    Args:
        stations (list): list of MonitoringStation objects 
        tol (float): minimum latest relative level needed

    Returns:
        list: list of tuples where each tuple holds a station object and the relative water level
    """
    stations_over_tol = []
    
    # Build a list of stations iwht inconsistent typical range data
    consistent_stations = consistent_typical_range_stations(stations)

    for station in consistent_stations:
        
        relative_water_level = MonitoringStation.relative_water_level(station)
        
        if relative_water_level is None:
            pass
        elif relative_water_level > tol:
            stations_over_tol.append((station.name, relative_water_level))
            i = station

    return sorted(stations_over_tol, key = lambda x:x[1], reverse=True)


def stations_highest_rel_level(stations, N):
    """Finds N stations at which the water level, relative to the typical range, is the highest

    Args:
        stations (list): list of MonitoringStation objects
        N (int): N number of stations with the highest water levels relative to the typical range

    Returns:
        list: stations with the highest water levels relative to the typical range
    """
    stations_with_highest_level = []
    # Build a list of stations wiht inconsistent typical range data
    consistent_stations = consistent_typical_range_stations(stations)
    
    for station in consistent_stations:
        relative_water_level = MonitoringStation.relative_water_level(station)

        if relative_water_level is None:
            pass
        else:
            stations_with_highest_level.append((station.name, relative_water_level))

    sorted_list = sorted(stations_with_highest_level, key=lambda x:x[1], reverse=True)
    return sorted_list[:N]



        