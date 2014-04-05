#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys

def main(args):
        data = np.load(args[0])
        plt.plot( np.abs( np.fft.fftshift( np.fft.fft(data["volts"]) ) ) )
        plt.title("Fourier-transformed voltage of " + args[1] + " over time", fontsize=36);
        plt.xlabel("Frequency (Hz)", fontsize=30)
        plt.ylabel("Fourier Power Coefficient", fontsize=30)
        plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
