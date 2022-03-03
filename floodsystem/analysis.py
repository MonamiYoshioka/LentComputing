import numpy as np

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
