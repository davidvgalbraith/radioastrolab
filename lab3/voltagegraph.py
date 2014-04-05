#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys

def main(args):
    data = np.load(args[0])
    plt.plot( data["volts"] )
    plt.title("Voltage of " + args[1] + " over time", fontsize=36);
    plt.xlabel("Time (sec)", fontsize=30)
    plt.ylabel("Voltage (V)", fontsize=30)
    plt.show()
    

if __name__ == "__main__":
    main(sys.argv[1:])
