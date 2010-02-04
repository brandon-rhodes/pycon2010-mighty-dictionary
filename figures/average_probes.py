import sys
import matplotlib.pyplot as plt

xa, ya1, ya2 = [], [], []
for line in open('figures/average_probes_data.txt'):
    x, y1, y2 = line.split()
    xa.append(float(x))
    ya1.append(float(y1))
    ya2.append(float(y2))

#print xa, ya1, ya2

plt.plot(xa, ya1, 'r')
plt.plot(xa, ya2, 'b')
plt.ylabel('Probes to find an index')
plt.savefig(sys.argv[1])
