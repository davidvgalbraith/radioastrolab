#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

def main(argv):

   sine = np.fromfile('cosin/sin_bram', dtype='>i4')
   cos = np.fromfile('cosin/cos_bram', dtype='>i4')

   x = np.fft.fftfreq(len(sine))

   plt.plot(x, abs(np.fft.fft(sine)), label="sine")
   plt.plot(x, abs(np.fft.fft(cos)), label="cos")

   plt.tick_params(axis='both', which='major', labelsize=24)
   plt.legend()
   plt.title("Crazy shit", fontsize=36)
   plt.xlabel("Frequency (MHz)", fontsize=36)
   plt.ylabel("Fourier Power Coefficient", fontsize=36)

   plt.show()

if __name__ == "__main__":
   main(sys.argv[1:])
