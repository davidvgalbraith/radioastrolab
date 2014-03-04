#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
   a = np.fft.fftfreq(2048)
   for x in range(1, 7):
      k = 10 * x
      imag = np.fromfile("ddc/ddc_imag_bram_" + k.__str__(), dtype=">i4")
      real = np.fromfile("ddc/ddc_real_bram_" + k.__str__(), dtype=">i4")
      ddddc = real + 1j * imag
      plt.plot(a, abs(np.fft.fft(ddddc)))
   plt.tick_params(axis='both', which='major', labelsize=24)
   
   plt.title("Filter response", fontsize=36)
   plt.xlabel("Input Frequency(MHz)", fontsize=36)
   plt.ylabel("Filter transfer V_out/V_in", fontsize=36)
   plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
