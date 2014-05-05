#!/usr/bin/python

import sys, getopt
import numpy as np
import matplotlib.pyplot as plt
import pylab

def matrify(lines):
   xes = []
   ys = []
   intensitys = []
   for q in lines:
      xes.append(q[0])
      ys.append(q[1])
      intensitys.append(q[2])
   m = np.zeros((10, 10))
   for k in np.arange(0, 10):
      m[round(xes[k])][round(ys[k])] += intensitys[k]
   return m


def main(argv):
   f = open("img_grid_data.txt")
   lines = np.array([map(float, line.split()) for line in f.readlines()[1:]])
   m = matrify(lines)
   pylab.imshow(m, origin="lower", interpolation="nearest", cmap="hot", vmax=5, vmin=4)
   pylab.colorbar()
   pylab.show()

if __name__ == "__main__":
   main(sys.argv[1:])

