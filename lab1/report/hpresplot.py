import matplotlib.pyplot as plt
import numpy as np
import math
x=[500,1000,2000,5000,10000,20000,50000]
y=[0.02,0.04,0.076,0.19,0.37,0.72,1.56]

plt.plot(x, [q/4 for q in y], 'ro')
plt.tick_params(axis='both', which='major', labelsize=24)

plt.xlabel("Frequency (Hz)", fontsize=30)
plt.ylabel("Vout / Vin", fontsize=30)
plt.title("Filter gain vs. Frequency for our Highpass Filter", fontsize=30)
plt.show()
