import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Created in task 2E
def plot_water_level(station, dates, levels):
    """Display a plot of the water level data against time for a station

    Args:
        station (object): station object
        dates (list): dates when the water level measurement were taken
        levels (list): water level measurements
    """
    
    water_level = levels
    time = dates
    
    # Plot the graph
    plt.plot(time, water_level, label="Water level")
    # Add lines for typical low and high levels
    plt.axhline(station.typical_range[1], color='g', label="Typical high")
    plt.axhline(station.typical_range[0], color='r', label="Typical low")
    
    # Add axix labels, rotate date labels, add title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    plt.title(f'Station: {station.name}')
    plt.legend()
    plt.tight_layout()
    
    plt.show()
    

# Created in Task 2F
def plot_water_level_with_fit(station, dates, levels, p):
    """Display a plot of the water level data against time for a station with a polyfit

    Args:
        station (object): station object
        dates (list): dates when the water level measurement were taken
        levels (list): water level measurements
        p (int): polynomial of degree p
    """
    
    # Convert list of datetime objects to a list of floats
    dates_floats = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(dates_floats, levels, p)
    
    plt.plot(dates, levels, '.' , label="Water level")
    
    x1 = np.linspace(d0, dates_floats[-1], 30)
    plt.plot(x1, poly(x1 - d0), label="Polyfit")
    
    # Add lines for typical low and high levels
    plt.axhline(station.typical_range[1], color='g', label="Typical high")
    plt.axhline(station.typical_range[0], color='r', label="Typical low")
    
    # Add axix labels, rotate date labels, add title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    plt.title(f'Station: {station.name}')
    plt.legend()
    plt.tight_layout()
    
    plt.show()