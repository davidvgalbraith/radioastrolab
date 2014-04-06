#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys

def main(args):
        data = np.load(args[0])["volts"]
        plt.plot( np.fft.fftfreq(len(data)), np.abs( np.fft.fft(data)))#np.fft.fftshift( np.fft.fft(data))))#["volts"]) ) ) )
        plt.title("Fourier-transformed signal of " + args[1] + " over time", fontsize=36);
        plt.xlabel("Frequency (Hz)", fontsize=30)
        plt.ylabel("Fourier Power Coefficient", fontsize=30)
	plt.tick_params(axis='both', which='major', labelsize=18)

        plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
