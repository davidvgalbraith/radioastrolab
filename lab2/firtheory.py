#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
   coeff = []
   coeff.append(0.239389)
   coeff.append(0.508846)
   coeff.append(0.759187)
   coeff.append(0.936155)
   coeff.append(1)
   coeff.append(0.936155)
   coeff.append(0.759187)
   coeff.append(0.508846)

   ffted = np.roll(np.fft.fft(coeff), 4)
   x = np.roll(np.fft.fftfreq(8), 4)
   y = [0, 0, 1, 1, 1, 1, 1, 0]
   plt.plot(x, abs(ffted), label="Filtration given by our coefficients")
   plt.plot(x, y, label="Ideal filter function")
   plt.tick_params(axis='both', which='major', labelsize=24)
   
   plt.title("Filter response", fontsize=36)
   plt.xlabel("Input Frequency(Hz)", fontsize=36)
   plt.ylabel("Filter transfer |V_out / V_in|", fontsize=36)
   plt.legend()
   plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
