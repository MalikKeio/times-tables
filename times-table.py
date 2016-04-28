#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Create Times Table!")
parser.add_argument('N', metavar='N', default=100, nargs='?', type=int,
                    help="Number of iterations (the highest, the prettiest). "
                    "If N is too high, you may only see a uniform big ball"
                    "because of aliasing depending on your screen resolution."
                    "Values between 10 and 1000 should work well, default is 100.")
parser.add_argument('-t', '--times', nargs=2, default=[2, 2], type=float,
                    help="Min and max of the 'times' factor.")

args = parser.parse_args()

import matplotlib.pyplot as plt
import matplotlib.collections as mc
import numpy as np


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

if args.times[0] == args.times[1]:
    times_table = TimesTable(args.times[0], args.N)
    times_table.add_to_axis(ax)

    plt.show()
else:
    raise "Not implemented"
