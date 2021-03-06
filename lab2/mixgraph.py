#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
   data = np.load('analogdsb/analog_mixing.npz')
   d = {}
   d["0"] = 1.05
   d["1"] = 0.95
   d["2"] = 105
   d["3"] = 95
   graphable = data["arr_" + argv[0]]
   ffted = np.fft.fft(graphable)
   x = np.arange(len(ffted))/200.0
   q = np.arange(len(ffted))/6.0
   ffted[0:5] = 0
   ffted[6:1024] = 0
   #print abs(ffted[0:12])
   inv = np.fft.ifft(ffted)
   xx = np.fft.fftfreq(len(graphable)) 
   #plt.plot(xx, abs(ffted))
   plt.plot(x, graphable)
   #plt.plot(q, inv)
   plt.tick_params(axis='both', which='major', labelsize=24)
   
   plt.title("Convoluted signal of 1MHz and " + d[argv[0]].__str__() + " MHz", fontsize=36)
   plt.xlabel("Time (microseconds)", fontsize=36)
   plt.ylabel("Signal", fontsize=36)
   #plt.title("Convoluted Power Spectrum of 1 MHz and " + d[argv[0]].__str__() + " MHz", fontsize=36)
   #plt.xlabel("Frequency(kHz)", fontsize=36)
   #plt.ylabel("Fourier Power Coefficient", fontsize=36)
   #plt.title("IFFT of convolved, filtered signals at 0.95 MHz and 1 MHz", fontsize=36)
   #plt.xlabel("Time (microsec)", fontsize=36)
   #plt.ylabel("Signal", fontsize=36)
   plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
