#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys

def main(args):
    data = np.load(args[0])
    volts = data["volts"][1700:3200]
    ffted = np.fft.fft(volts)
    freaks = np.fft.fftfreq(len(volts))
    for k in range(0, len(freaks)):
        if (abs(freaks[k]) > 0.0203 or abs(freaks[k]) < .01):
            ffted[k] = 0
    plt.plot( np.fft.ifft(ffted))
    plt.title("Filtered signal of " + args[1] + " over time", fontsize=36);
    plt.xlabel("Time (sec)", fontsize=30)
    plt.ylabel("Signal strength", fontsize=30)
    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.show()
    

if __name__ == "__main__":
    main(sys.argv[1:])
