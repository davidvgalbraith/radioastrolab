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
   x = np.fft.fftfreq(len(data)) * 200 
   xx = np.arange(0, len(data)) / 200.0
   ffted = np.fft.fft(data)
   
   #plt.plot(x, abs(ffted))
   plt.plot(xx, data)
   #plt.plot(xx, ffted)
   plt.tick_params(axis='both', which='major', labelsize=24)
   plt.title("Convoluted signal of 1 MHz and 0.95 MHz", fontsize=36)
   plt.xlabel("Time (microsec)", fontsize=36)
   plt.ylabel("Signal", fontsize=36)
   #plt.title("Digitally Convoluted Power Spectrum of 1 MHz and 1.05 MHz", fontsize=36)
   #plt.xlabel("Frequency(MHz)", fontsize=36)
   #plt.ylabel("Power Amplitude Coefficient", fontsize=36)
 
   plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
