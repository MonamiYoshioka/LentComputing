import matplotlib.pyplot as plt

# Created in task 2E
def plot_water_level(station, dates, levels):
    """Display a plot of the water level data against time for a station

    Args:
        station (string): name of the station
        dates (list): dates when the water level measurement were taken
        levels (list): water level measurements
    """
    
    water_level = levels
    time = dates
    
    # Plot the graph
    plt.plot(time, water_level)
    
    # Add axix labels, rotate date labels, add title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    plt.title(f'Station {station}')
    plt.tight_layout()
    
    plt.show()