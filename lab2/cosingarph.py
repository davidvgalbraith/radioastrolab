#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

def main(argv):

   sine = np.fromfile('cosin/sin_bram', dtype='>i4')
   cos = np.fromfile('cosin/cos_bram', dtype='>i4')
   comb = cos + 1j * sine
   #x = np.fft.fftfreq(len(comb)) * 200000
   x = np.arange(0, len(sine)) / 200.
   #plt.plot(x, abs(np.fft.fft(comb)))
   plt.plot(x, cos, label="Real part (cos)")
   plt.plot(x, sine, label="Imaginary part (sin)")

   plt.tick_params(axis='both', which='major', labelsize=24)
   plt.legend()
   plt.title("Waveform for SSB-combined 1 MHz and 1.56 MHz", fontsize=36)
   plt.xlabel("Time (microseconds)", fontsize=36)
   plt.ylabel("Voltage", fontsize=36)

   plt.show()

if __name__ == "__main__":
   main(sys.argv[1:])
