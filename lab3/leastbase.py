import sys
import numpy as np
import matplotlib.pyplot as plt

def matrify(data, power):
    n = data.size
    X = []
    for a in range(0, power+1):
        X.append(data ** a)
    return np.transpose(np.matrix(X))

def matrificate(hours, guess):
    X = []
    X.append(np.cos(2 * np.pi * guess * np.sin(hours) * np.cos(.4) / .025))
    X.append(-np.sin(2 * np.pi * guess * np.sin(hours) * np.cos(.4) / .025))
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
    q = coeff[0, 0] * np.cos(2 * np.pi * guess * np.sin(x) * np.cos(.4) / .025) - coeff[1, 0] * np.sin(2 * np.pi * guess * np.sin(x) * np.cos(.4) / .025)
    return q

def curvificate(x, coeff, guess):
    q = coeff[0] * np.cos(2 * np.pi * guess * np.sin(x) * np.cos(.4) / .025) - coeff[1] * np.sin(2 * np.pi * guess * np.sin(x) * np.cos(.4) / .025)
    return q
#Brewt force least squares for baseline
def main(argv):
    data = np.load("data/3C144_03-28-2014_001926.npz")
    xvals = data["lst"]
    xvals = xvals[5:len(xvals)-5]
    print xvals
    hourangles = 2 * np.pi / 24 * (xvals - 5.6)
    yvals = data["volts"]
  #  plt.plot(yvals)
   # plt.show()

    yvals = (yvals[5:len(yvals) - 5] - boxcar(yvals)) * 1000000
 #   plt.plot(yvals)
#    plt.show()

    ffted = np.fft.fft(yvals)
    freaks = np.fft.fftfreq(len(ffted))
    for k in range(0, len(freaks)):
        if (abs(freaks[k]) > 0.0203 or abs(freaks[k]) < 0.01):
            ffted[k] = 0
    yvals = np.fft.ifft(ffted).real
    plt.plot(yvals, label="Measured data")
    plt.xlabel("Time (sec)", fontsize=30)
    plt.ylabel("Signal", fontsize=30)
    plt.title("Filtered, smoothed Crab signal", fontsize = 36)
    plt.plot(curvificate(hourangles, [-0.41, 0.41], 9.114), label="Fitted curve")
    plt.legend()
    plt.show()

    print hourangles
    xgarphvals = []
    ygarphvals = []
    minum = 9999999999999999999
    dictum = {}
    delta = 0.0001
    for guess in np.arange(9.08, 9.14, delta):
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
        if cheese < minum:
            minum = cheese
            dictum[cheese] = coeffab
        print guess, cheese
        ygarphvals.append(cheese)
    plt.plot(xgarphvals, ygarphvals)
    print dictum[minum]
    #plt.plot(hourangles, yvals)
    plt.xlabel("Guess of proper value for Baseline (m)", fontsize=30)
    plt.ylabel("Chi-square error", fontsize=30)
    plt.title("Error as a function of guessed Baseline", fontsize = 36)
    plt.legend()
    plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
