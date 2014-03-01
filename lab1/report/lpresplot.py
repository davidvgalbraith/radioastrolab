import matplotlib.pyplot as plt
import numpy as np
import math

x = [10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000]

y=[4,4,4,4,4,4,4,4,4,4,3.9,3.35,2.5,1.44,0.84,0.29]


plt.plot([a/1000 for a in x], [q/4 for q in y], 'ro')
plt.tick_params(axis='both', which='major', labelsize=24)
plt.xlabel("Frequency (kHz)", fontsize=32)
plt.ylabel("Vout / Vin", fontsize=32)
plt.title("Filter gain vs. Frequency for our Lowpass Filter", fontsize = 32)
plt.show()
