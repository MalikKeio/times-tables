#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.collections as mc
import numpy as np

N = 100
times = 2

ax = plt.axes()

segments = np.zeros(N, list)

for i in range(N):
    x0 = np.cos(i*2*np.pi/N)
    y0 = np.sin(i*2*np.pi/N)
    x1 = np.cos(times*i*2*np.pi/N)
    y1 = np.sin(times*i*2*np.pi/N)
    segments[i] = [(x0, y0), (x1, y1)]

line_collection = mc.LineCollection(segments)
ax.add_collection(line_collection)
ax.autoscale()
ax.margins(0.1)
ax.set_aspect('equal')

plt.show()
