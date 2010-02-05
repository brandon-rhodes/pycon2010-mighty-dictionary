import sys
import matplotlib.pyplot as plt

xa, ya1, ya2 = [], [], []
for line in open('figures/average_probes_data.txt'):
    x, y1, y2 = line.split()
    xa.append(float(x))
    ya1.append(float(y1))
    ya2.append(float(y2))

plt.plot(xa, ya1, 'r', lw=3)
plt.text(1300, 2.5, 'average', color='r', fontsize=30)

plt.plot(xa, ya2, 'c', lw=3)
plt.text(1300, 9, 'worst', color='c', fontsize=30)

plt.plot([0, 3000], [1, 1], 'k--', lw=1)
plt.plot([0, 3000], [2, 2], 'k--', lw=1)
plt.axis([0, 3000, 0, 20])
plt.ylabel('Probes per getitem', fontsize=24)
plt.savefig(sys.argv[1], dpi=60)
