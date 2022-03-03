import numpy as np
import matplotlib
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
import datetime

# Created in Task 2F
def polyfit(dates, levels, p):
    """Given the water level time history for a station, it computes least-squares
    fit of a polynomial of degree p to water level data

    Args:
        dates (datetime): list of dates
        levels: list of water levels
        p (int): polynomial of degree p

    Returns:
        tuple: (polynomial object, shift of date axis)
    """
    
    p_coeff = np.polyfit(dates - dates[0], levels, p)
    
    # Create a numpy.poly1d object
    poly = np.poly1d(p_coeff)
    
    return poly, dates[0]


def gradient_analysis(dates, levels, p):
    """Finds value of gradient of the polyfit at the most recent date
    If the gradient is positive, water level is rising

    Args:
        dates (datetime): list of dates
        levels: list of water levels
        p (int): polynomial of degree p

    Returns:
        float: value of dy/dx for the most recent value
    """
    dates_floats = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(dates_floats, levels, p)
    
    x1 = np.linspace(d0, dates_floats[-1], 30)
    y = poly(x1 - d0)
    dydx = np.diff(y)/np.diff(x1)
    
    return dydx[-1]

def create_flood_risk_list(stations, tol, gradient_thresh):
    severe = []
    high = []
    moderate = []
    low = []
    
    # Find stations whose current high levels are above the tolerance (SEVERE, HIGH and MODERATE risks)
    station_relative_level_over_tol = []
    station_threshold = stations_level_over_threshold(stations, tol)
    for station in station_threshold:
        station_relative_level_over_tol.append(station)
    
    # Check wether the polyfit gradient is above or below zero
    # If above zero, water level is rising
    dt = 2
    for station in stations:
        if station.name in (i[0] for i in station_relative_level_over_tol):
            dates, level = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            try:
                gradient = gradient_analysis(dates, level, 4)
                if gradient > gradient_thresh:
                    severe.append(station)
                    station.gradient = gradient
                else:
                    high.append(station)
                    station.gradient = gradient
            except:
                pass
        else:
            try:
                gradient = gradient_analysis(dates, level, 4)
                if gradient > gradient_thresh:
                    moderate.append(station)
                    station.gradient = gradient
                else:
                    low.append(station)
                    station.gradient = gradient
            except:
                pass
    
    return severe, high[:5], moderate[:5], low[:5]