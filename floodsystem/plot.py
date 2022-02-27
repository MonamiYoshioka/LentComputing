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