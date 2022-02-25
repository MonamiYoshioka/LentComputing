import matplotlib as plt

# Created in task 2E
def plot_water_level(station, dates, levels):
    water_level = []
    time = []
    
    # Plot the graph
    plt.plot(time, water_level)
    
    # Add axix labels, rotate date labels, add title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    plt.title(f'Station {station.name}')
    plt.tight_layout()
    
    plt.show()