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
parser.add_argument('-s', '--speed', type=float, default=10, help="The higher the faster. 100 is very fast, 1 is quite slow.")
parser.add_argument('-o', '--output', type=str, help="Output as a mp4 file.")
parser.add_argument('-b', '--bitrate', type=float, default=8192, help="Bitrate (bit/s) for mp4 output. Default is 8192.")

args = parser.parse_args()

if args.output is not None:
    import matplotlib
    matplotlib.use("Agg")
    if args.bitrate is not None:
        matplotlib.rcParams['animation.bitrate'] = args.bitrate

import matplotlib.pyplot as plt
import matplotlib.collections as mc
import numpy as np

ax = plt.axes()
ax.set_aspect('equal')
ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])

class TimesTable:
    def __init__(self, times=2, N=100):
        self._N = N
        self._line_collection = mc.LineCollection(TimesTable._get_segments(times, N))

    def add_to_axis(self, ax, **kwargs):
        ax.add_collection(self._line_collection, kwargs)

    def set_times(self, times):
        self._line_collection.set_segments(TimesTable._get_segments(times, self._N))

    @staticmethod
    def _get_segments(times, N):
        segments = np.zeros(N, list)
        for i in range(N):
            x0 = np.cos(i*2*np.pi/N)
            y0 = np.sin(i*2*np.pi/N)
            x1 = np.cos(times*i*2*np.pi/N)
            y1 = np.sin(times*i*2*np.pi/N)
            segments[i] = [(x0, y0), (x1, y1)]
        return segments

class AnimatedTimesTable(TimesTable):
    def __init__(self, times=[2, 100], N=100, speed=0.01, interval=40):
        self._times = times
        TimesTable.__init__(self, times[0], N)
        self._interval = interval
        self._speed = speed
        self._frame_count = 0

    def _animate(self, t):
        self.set_times(t)
        if self._headless:
            if self._frame_count != self._frame_number:
                print("Frame: %d/%d\r" % (self._frame_count, self._frame_number), end='')
            else:
                print("DONE                      ")
        self._frame_count += 1

    def add_to_axis(self, ax, **kwargs):
        filename = kwargs.get('output', None)
        self._headless = filename is not None
        TimesTable.add_to_axis(self, ax, **kwargs)
        arange = np.arange(self._times[0], self._times[1], (self._times[1] - self._times[0]) * self._speed)
        self._frame_number = 1 / self._speed
        ani = animation.FuncAnimation(ax.figure, self._animate, arange, interval=self._interval)
        if self._headless:
            Writer = animation.writers['ffmpeg']
            writer = Writer(fps=25, metadata=dict(artist='Malik Olivier Boussejra'))
            ani.save(filename, writer=writer)



if args.times[0] == args.times[1] or args.speed == 0:
    times_table = TimesTable(args.times[0], args.N)
    times_table.add_to_axis(ax)

    plt.show()
else:
    from matplotlib import animation
    times_table = AnimatedTimesTable(args.times, args.N, args.speed/1000)
    times_table.add_to_axis(ax, output=args.output)
    if args.output is None:
        plt.show()
