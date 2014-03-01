import matplotlib.pyplot as plt
import numpy as np
import math

def f(vin):
    c = 2.2e-8
    r = 150
    q = 1.0/math.sqrt(1 + vin*vin * c*c * r*r)
    return q

x = np.arange(1, 600000L, 5)
y = map(f, x)

plt.plot(x/(2 * math.pi), y)
plt.tick_params(axis='both', which='major', labelsize=28)

plt.title("Theoretical response of a Low-pass Filter", fontsize=36)
plt.xlabel("Frequency (Hz)", fontsize=36)
plt.ylabel("Filter gain", fontsize=36)
plt.show()
