import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Created in Task 2F
def polyfit(dates, levels, p):
    dates = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(dates - dates[0], levels, p)
    
    poly = np.poly1d(p_coeff)
    
    plt.plot(dates, levels, '.')
    
    x1 = np.linspace(dates[0], dates[-1], 30)
    plt.plot(x1, poly(x1 - dates[0]))
    
    plt.show()

