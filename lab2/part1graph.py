#!/usr/bin/python

import sys, getopt
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
   data = np.load('sampling1/lab_digital_sampling.npz')
   d = {}
   d["0"] = 3.0
   d["1"] = 0.4
   d["2"] = 0.7
   d["3"] = 0.9
   d["4"] = 1
   d["5"] = 0.1
   graphable = data["arr_" + argv[0]]
   x = np.arange(0, len(graphable), 1)
   
   plt.plot(x, graphable)
   plt.tick_params(axis='both', which='major', labelsize=24)
   
   plt.title("Sampled Waveform for " + d[argv[0]].__str__() + " times Nyquist Frequency", fontsize=36)
   plt.xlabel("Sample (time instant)", fontsize=36)
   plt.ylabel("Measured Voltage", fontsize=36)
   plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
