#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
   sine = np.fromfile('cosin/sin_bram', dtype='>i4')
   cos = np.fromfile('cosin/cos_bram', dtype='>i4')
   x = np.fft.fftfreq(len(sine))
   plt.plot(x, abs(np.fft.fft(sine)))
   plt.plot(x, abs(np.fft.fft(cos)))
   plt.tick_params(axis='both', which='major', labelsize=24)
   
   #plt.title("Convoluted signal of 1MHz and " + d[argv[0]].__str__() + " MHz", fontsize=36)
   #plt.xlabel("Time instant (sample #)", fontsize=36)
   #plt.ylabel("Signal", fontsize=36)
   #plt.title("Convoluted Power Spectrum of 1 MHz and " + d[argv[0]].__str__() + " MHz", fontsize=36)
   #plt.xlabel("Frequency(kHz)", fontsize=36)
   #plt.ylabel("Power Amplitude Coefficient", fontsize=36)
   plt.title("Crazy shit", fontsize=36)
   plt.xlabel("Time (sec)", fontsize=36)
   plt.ylabel("Signal", fontsize=36)
   plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
