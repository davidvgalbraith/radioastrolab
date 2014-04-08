#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys

def matrify(data, power, eft):
    n = data.size
    X = []
    for a in range(0, power+1):
        X.append((data ** a) * eft)
    return np.transpose(np.matrix(X))

def curvify(hour, coeffab, eft):
	return coeffab[0, 0] * eft + coeffab[1, 0] * eft * hour + coeffab[2, 0] * eft * hour**2

def chisquare(arr):
    total = 0;
    for xx in arr:
        total += xx ** 2
    return total

def indexofclosesthourangle(hourangles, x):
    diff = 9999
    ret = 0
    for k in np.arange(0, len(hourangles), 1):
        if np.abs(hourangles[k] - x) < diff:
            diff = np.abs(hourangles[k] - x)
            ret = k
    return ret

def mftheory(ff, N):
    rvals = []
    errs = []
    for r in np.arange(0, .01, 0.00001):
        print r
        mft = 0
        for n in np.arange(-N, N, 1):
            mft += np.sqrt(1 - (n / N)**2) * np.cos(2 * np.pi * ff * r * n / N)
        rvals.append(r)
        errs.append(r / N * mft)
    plt.plot(rvals, errs)
    plt.xlabel("Guessed r-value (Radians)", fontsize=30)
    plt.ylabel("MFT", fontsize=30)
    plt.title("MFT versus guessed angular radius", fontsize=36)
    plt.show()

def main(args):
        data = np.load("data/moon_04-06-2014_033444.npz")
	lsts = np.array(data["lst"][1700:3200])
	ras = np.array(data["ra"][1700:3200])
	decs = np.array(data["dec"][1700:3200]) * np.pi / 180
	hourangles = (2 * np.pi / 24) * (lsts - ras)
	volts = data["volts"][1700:3200]
        ffted = np.fft.fft(volts)
        freaks = np.fft.fftfreq(len(volts))
        for k in range(0, len(freaks)):
            if (abs(freaks[k]) > 0.0203 or abs(freaks[k]) < .01):
                ffted[k] = 0
        yvals = np.fft.ifft(ffted).real
	xgarphvals = []
	ygarphvals = []
        min = 1000000000000000000000
        junk = 12
        k = indexofclosesthourangle(hourangles, 2.34)
        #print k
        #print hourangles[k]
        #print decs[k]
        ff = 345.0 * np.cos(decs[k]) * np.cos(hourangles[k])
        print ff
        mftheory(ff, 1000)
	return
        for guess in np.arange(2.619,np.pi, 10):
		xgarphvals.append(guess)
		eft = np.cos(345 * np.pi * 2 *  np.cos(decs) * np.sin(hourangles) + guess) / 10000
                #plt.plot(hourangles, eft, label="EFT")
		xmatrix = matrify(hourangles, 2, eft)
		xtrans = np.transpose(xmatrix)
		atb = np.transpose(np.dot(xtrans, yvals))
		ata = np.dot(xtrans, xmatrix)
		coeffab = np.linalg.solve(ata, atb)
		print guess, coeffab
		line = curvify(hourangles, coeffab, eft)
		plt.plot(hourangles, line, label="Best fit")
		residuals = abs(line - yvals)
		cheese = chisquare(residuals)
                if cheese < min:
                    min = cheese
                    junk = guess
		ygarphvals.append(cheese)
        print junk
	plt.plot(hourangles, yvals, label="Yvals")
        plt.xlabel("Guessed value of angle offset (rad)", fontsize=30)
        plt.ylabel("Chi-Squared error", fontsize=30)
        plt.title("Chi-squared error as a function of guessed Angle offset", fontsize=36)
	#plt.plot(xgarphvals, ygarphvals)	
        plt.legend()
	plt.show()

def mf(ff, r, n):
	sum = 0
	for k in range(-n, n):
		sum = sum + ((1 - (k/n)**2)**0.5) * np.cos(ff * r * 2 * np.pi * k / n)
	return sum
if __name__ == "__main__":
    main(sys.argv[1:])
