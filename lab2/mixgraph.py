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
   x = np.arange(0, len(graphable), 1)
   xx = np.fft.fftfreq(len(graphable)) 
   y = np.arange(0, len(ffted), 1)
   plt.plot(xx, abs(ffted))
   #plt.plot(x, graphable)
   plt.tick_params(axis='both', which='major', labelsize=24)
   
   #plt.title("Convoluted signal of 1MHz and " + d[argv[0]].__str__() + " MHz", fontsize=36)
   #plt.xlabel("Time instant (sample #)", fontsize=36)
   #plt.ylabel("Signal", fontsize=36)
   plt.title("Convoluted Power Spectrum of 1 MHz and " + d[argv[0]].__str__() + " MHz", fontsize=36)
   plt.xlabel("Frequency(MHz)", fontsize=36)
   plt.ylabel("Power Amplitude Coefficient", fontsize=36)
   plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
