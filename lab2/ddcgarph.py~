#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
   d = {}
   d["0"] = "high"
   d["1"] = "low"
   data = np.fromfile("roach/twelve/mix_bram_" + d[argv[0]] + "_sig_5pct_12dbm", dtype=np.int32)
   #data = np.fromfile("roach/mix_bram_" + d[argv[0]] + "_sig_10pct", dtype=">i4")
   #data = np.fromfile("roach/adc_bram_1", dtype=">i4")
   print len(data)
   x = np.arange(len(data))
   ffted = np.fft.fft(data)
   inv = np.fft.ifft(ffted)
   xx = np.fft.fftfreq(len(data)) 
   print inv
   plt.plot(xx, abs(ffted))
   #plt.plot(x, data)
   #plt.plot(xx, ffted)
   plt.tick_params(axis='both', which='major', labelsize=24)
   
   #plt.title("Convoluted signal of 1MHz and " + d[argv[0]].__str__() + " MHz", fontsize=36)
   #plt.xlabel("Time instant (sample #)", fontsize=36)
   #plt.ylabel("Signal", fontsize=36)
   plt.title("Digitally Convoluted Power Spectrum of 1 MHz and 1.05 MHz", fontsize=36)
   plt.xlabel("Frequency(MHz)", fontsize=36)
   plt.ylabel("Power Amplitude Coefficient", fontsize=36)
   #plt.title("IFFT of convolved, filtered signals at 0.95 MHz and 1 MHz", fontsize=36)
   #plt.xlabel("Time (sec)", fontsize=36)
   #plt.ylabel("Signal", fontsize=36)
   plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
