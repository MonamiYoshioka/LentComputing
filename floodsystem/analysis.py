import numpy as np
import matplotlib

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