# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def create_line_charts(data, title, exported_fig_filename):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    prices = (sorted(map(float,data)))
    
    x_axis_ticks = list( range(len(data)))
    ax.plot(x_axis_ticks, prices, linewidth = 2)
    ax.set_title(title)
    ax.set_xlim([0, len(data)])
    ax.set_xlabel('Tie Prices($)')
    ax.set_ylabel('Number of Ties')
    