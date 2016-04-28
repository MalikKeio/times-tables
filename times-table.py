#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.collections as mc
import numpy as np

N = 100
times = 2

ax = plt.axes()
ax.set_aspect('equal')
ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])

class TimesTable:
    def __init__(self, times=2, N=100):
        segments = np.zeros(N, list)
        for i in range(N):
            x0 = np.cos(i*2*np.pi/N)
            y0 = np.sin(i*2*np.pi/N)
            x1 = np.cos(times*i*2*np.pi/N)
            y1 = np.sin(times*i*2*np.pi/N)
            segments[i] = [(x0, y0), (x1, y1)]
        self._line_collection = mc.LineCollection(segments)

    def add_to_axis(self, ax, **kwargs):
        ax.add_collection(self._line_collection, kwargs)

times_table = TimesTable(times, N)
times_table.add_to_axis(ax)

plt.show()
