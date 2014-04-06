#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys

def main(args):
    data = np.load(args[0])
    plt.plot( data["volts"] )
    plt.title("Signal of " + args[1] + " over time", fontsize=36);
    plt.xlabel("Time (sec)", fontsize=30)
    plt.ylabel("Signal strength", fontsize=30)
    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.show()
    

if __name__ == "__main__":
    main(sys.argv[1:])
