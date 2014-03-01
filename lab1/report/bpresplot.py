import matplotlib.pyplot as plt
import numpy as np
import math

x = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
y = [.028, .052, 0.128, .25, .48, 1.08, 1.56, 1.85, 1.95, 2.5]

plt.plot(x, [q/4 for q in y], 'ro')
plt.xlabel("Frequency (Hz)", fontsize=20)
plt.ylabel("Vout / Vin", fontsize=20)
plt.title("Filter gain vs. Frequency for our Bandpass Filter")
plt.show()
