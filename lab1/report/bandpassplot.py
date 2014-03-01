import matplotlib.pyplot as plt
import numpy as np
import math

def square(x):
    return x * x

def f(vin):
    c = 2.2e-8
    r = 33.0
    l = 1e-6
    q = (vin * l / math.sqrt(square(r * (1 - square(vin) * l * c)) + square(vin * l)))
    return q

x = np.arange(5000000L, 12000000L, 1000)
y = map(f, x)

plt.plot((x / (2 * math.pi))/1000, y)

plt.vlines(1045, 0.2, 1)
plt.tick_params(axis='both', which='major', labelsize=24)

plt.title("Theoretical response of our Band-pass Filter", fontsize = 36)
plt.xlabel("Frequency (kHz)", fontsize = 36)
plt.ylabel("Filter gain", fontsize = 36)
plt.show()
