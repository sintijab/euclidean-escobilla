from scipy.io import wavfile
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

fs1, data1 = wavfile.read("buleriaestrellamorente.wav")
fs2, data2 = wavfile.read("buleriamarinaheredia.wav")
fs3, data3 = wavfile.read("seguirillagemajimenez.wav")
fs4, data4 = wavfile.read("carmen.wav")

plt.style.use('seaborn-whitegrid')
ax = plt.subplot(111)
ax.plot(data1, 'g-', alpha=0.2)
ax.plot(data2, 'g-', alpha=0.2)
ax.plot(data3, 'g-', alpha=0.2)

data1 = np.amax(data1, axis=1)
data2 = np.amax(data2, axis=1)
data3 = np.amax(data3, axis=1)
data4 = np.amax(data4, axis=1)

d1 = fastdtw(data4, data1)[0]
d2 = fastdtw(data4, data2)[0]
d3 = fastdtw(data4, data3)[0]

plt.savefig('plot2.png', dpi=600)

f = open("test.txt", "w")
f.write("The distance between the Carmen escobilla por Bulerias and Estrella Morente Bulerias (30s): %s" % d1)
f.write("\n")
f.write("The distance between the Carmen escobilla por Bulerias and Marina Heredia Bulerias (30s): %s" % d2)
f.write("\n")
f.write("The distance between the Carmen escobilla por Bulerias and Gema Jimenez Seguirilla (30s): %s" % d3)
f.write("\n")
f.close()
