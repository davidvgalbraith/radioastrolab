import sys
import numpy as np
import matplotlib.pyplot as plt
import math 

def matrify(data, power):
    n = data.size
    X = []
    for a in range(0, power+1):
        X.append(data ** a)
    return np.transpose(np.matrix(X))

def matrificate(hours, guess):
    X = []
    X.append([math.cos(2 * math.pi * guess * math.sin(x) * math.cos(.4) / .025) for x in hours]) 
    X.append([-math.sin(2 * math.pi * guess * math.sin(x) * math.cos(.4) / .025) for x in hours])
    return np.transpose(np.matrix(X));

def polynomial(x, coeff):
    ret = 0
    for k in range(0, len(coeff)):
        ret += coeff[k] * x ** k
    return ret

def chisquare(arr):
    total = 0;
    for xx in arr:
        total += xx ** 2
    return total

def average(arr):
    total = 0.0;
    for x in arr:
        total += x;
    return total / len(arr)

def boxcar(raw):
    smoothed = []
    for k in range(5, len(raw) - 5):
        smoothed.append(sorted(raw[k-5:k+6])[5])
    return smoothed

def curvify(x, coeff, guess):
    q = coeff[0, 0] * math.cos(2 * math.pi * guess * math.sin(x) * math.cos(.4) / .025) - coeff[1, 0] * math.sin(2 * math.pi * guess * math.sin(x) * math.cos(.4) / .025)
    return q
#Brewt force least squares for baseline
def main(argv):
    data = np.load("data/3C144_03-28-2014_001926.npz")
    xvals = data["lst"][2000:8100]
    xvals = xvals[5:len(xvals)-5]
    print xvals
    hourangles = 2 * math.pi / 24 * (xvals - 5.6)
    yvals = data["volts"][2000:8100]
    plt.plot(yvals)
    plt.show()

    yvals = (yvals[5:len(yvals) - 5] - boxcar(yvals)) * 1000000
    plt.plot(yvals)
    plt.show()

    ffted = np.fft.fft(yvals)
    freaks = np.fft.fftfreq(len(ffted))
    for k in range(0, len(freaks)):
        if (abs(freaks[k]) > 0.0203 or abs(freaks[k]) < 0.01):
            ffted[k] = 0
    yvals = np.fft.ifft(ffted).real
    plt.plot(yvals)
    plt.show()

    print hourangles
    xgarphvals = []
    ygarphvals = []
    delta = 0.001
    for guess in np.arange(8, 11, delta):
        xgarphvals.append(guess)
        xmatrix = matrificate(hourangles, guess)
        xtrans = np.transpose(xmatrix)
        atb = np.transpose(np.dot(xtrans, yvals))
        ata = np.dot(xtrans, xmatrix)
        coeffab = np.linalg.solve(ata, atb)
        line = [curvify(hour, coeffab, guess) for hour in hourangles]
        #plt.plot(hourangles, line, label=guess.__str__())
        residuals = abs(line - yvals)
        print max(residuals)
        cheese = chisquare(residuals)
        print guess, cheese
        ygarphvals.append(cheese)
    plt.plot(xgarphvals, ygarphvals)
    #plt.plot(hourangles, yvals)
    plt.xlabel("Guess of proper value for By/lambda * cos(delta)", fontsize=30)
    plt.ylabel("Chi-square error", fontsize=30)
    plt.title("Error as a function of guessed C", fontsize = 36)
    plt.legend()
    plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
