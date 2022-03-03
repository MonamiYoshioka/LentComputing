from floodsystem.stationdata import MonitoringStation
# Create own dataset for testing purposes

def get_madeup_station_list():
    stations = []
    station1 = MonitoringStation("test_sid_1", "test_mid_1", 1, (51, -1), (0.1, 0.2), 'River1', 'Town1')
    station2 = MonitoringStation("test_sid_2", "test_mid_2", 2, (52, 0), (0.3, 0.4), 'River2', 'Town1')
    station3 = MonitoringStation("test_sid_3", "test_mid_3", 3, (51, -2), (0.5, 0.6), 'River3', 'Town3')
    station4 = MonitoringStation("test_sid_4", "test_mid_4", 4, (50, -2), None, 'River3', 'Town3')
    station5 = MonitoringStation("test_sid_4", "test_mid_4", 4, (50, -2), (0.5, 1.0), 'River4', 'Town5')
    
    station1.latest_level = 0.5
    station2.latest_level = 0.35
    station3.latest_level = 0.7
    station4.latest_level = 0.3
    station5.latest_level = 2.0
    
    stations.append(station1)
    stations.append(station2)
    stations.append(station3)
    stations.append(station4)
    stations.append(station5)
    return stations