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
   ffted = np.fft.fft(comb)
   ffted[len(ffted)/15:len(ffted)] = 0
   ffted[0:len(ffted)/16]=0
   ffted[len(ffted)/16:len(ffted)/15-2] = 0
   ffted[len(ffted)/15-1] = 0
   print abs(ffted[len(ffted)/16:len(ffted)/15])
   inv = np.fft.ifft(ffted) * 50
   plt.plot(x, inv, label="Desired sum frequency")
   plt.tick_params(axis='both', which='major', labelsize=24)
   plt.legend()
   plt.title("Waveform for SSB-mixed 10 MHz and 6.25 MHz", fontsize=36)
   plt.xlabel("Time (microseconds)", fontsize=36)
   plt.ylabel("Voltage", fontsize=36)
   #plt.title("Power Spectrum for SSB-mixed 10 MHz and 6.25 MHz", fontsize=36)
   #plt.xlabel("Frequency (kHz)", fontsize=36)
   #plt.ylabel("Fourier power coefficient", fontsize=36)

   plt.show()

if __name__ == "__main__":
   main(sys.argv[1:])
