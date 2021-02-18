import matplotlib.pyplot as plt
import numpy as np
import sys

with open("sample-data-metronome", "r") as fd:
    list1 = [map(float, line.split())[0] for line in fd]

with open("sample-data-music", "r") as m:
    list2 = [map(float, line.split())[0] for line in m]

def average(arr, n):
    remainder = len(arr) % n
    if remainder == 0:
        avg = np.mean(arr.reshape(-1, n), axis=1)
        return avg
    else:
        avg_head = np.mean(arr[:-remainder].reshape(-1, n), axis=1)
        avg_tail = np.mean(arr[-remainder:])
        avg_tail = np.repeat(avg_tail, remainder)
        return np.append(avg_head, avg_tail)

s1 = average(np.array(list1), 1000)
s2 = average(np.array(list2), 1000)
index = [i for i, x in enumerate(s1)]

fig = plt.figure(figsize=(60, 20))
ax1 = fig.add_subplot(111)

t = np.array(index)
ax1.plot(t, s1, 'b-')
ax1.set_xlabel('Length processed: (500 avg samples from 500000), 10.41667 seconds')

ax1.set_ylabel('Peak amplitude: 0.37104 (linear) -8.61169 dB', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(t, s2, 'r--')
ax2.set_ylabel('sin', color='r')
ax2.tick_params('y', colors='r')

plt.savefig('plot.png', dpi=600)
