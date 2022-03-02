from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels


def stations_highest_rel_level(stations, N):
    pass


def stations_level_over_threshold(stations,tol):

    update_water_levels(stations)

    stations_over_tol = []

    

    for station in stations:
        relative_water_level = MonitoringStation.relative_water_level(station)

        if relative_water_level > tol:
            stations_over_tol.append((station.name, relative_water_level))

        elif relative_water_level is None:
            pass

    return sorted(stations_over_tol, key = lambda x:x[1])

def stations_highest_rel_level(stations, N):

    stations_with_highest_level = []

    for station in stations:
        relative_water_level = MonitoringStation.relative_water_level(station)

        if relative_water_level is None:
            pass
        else:
            stations_with_highest_level.append(station.name, relative_water_level)

    return sorted(stations_with_highest_level, key=lambda x:x[1])




        