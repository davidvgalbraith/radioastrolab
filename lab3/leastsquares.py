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
    X.append([math.cos(2 * math.pi * guess * math.sin(x)) for x in hours]) 
    X.append([-math.sin(2 * math.pi * guess * math.sin(x)) for x in hours])
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

def curvify(x, coeff, guess):
    q = coeff[0, 0] * math.cos(2 * math.pi * guess * math.sin(x)) - coeff[1, 0] * math.sin(2 * math.pi * guess * math.sin(x))
    return q
#Brought force least squares
def main(argv):
    data = np.load("data/3C144_03-28-2014_001926.npz")
    xvals = data["lst"]
    hourangles = 2 * math.pi / 24 * (xvals - 5.09655)
    yvals = (data["volts"] - average(data["volts"]))
    xgarphvals = []
    ygarphvals = []
    delta = 1
    for guess in np.arange(30, 50, delta):
        xgarphvals.append(guess)
        xmatrix = matrificate(hourangles, guess)
        xtrans = np.transpose(xmatrix)
        atb = np.transpose(np.dot(xtrans, yvals))
        ata = np.dot(xtrans, xmatrix)
        coeffab = np.linalg.solve(ata, atb)
        line = [curvify(hour, coeffab, guess) for hour in hourangles]
        plt.plot(xvals, line, label=guess.__str__())
        residuals = abs(line - yvals)#abs(np.array(line)[0] - yvals)
        print max(residuals)
        cheese = chisquare(residuals)
        print guess, cheese
        ygarphvals.append(cheese)
    #plt.plot(xgarphvals, ygarphvals)
    plt.plot(xvals, yvals)
    plt.xlabel("Guess of proper value for By/lambda * cos(delta)", fontsize=30)
    plt.ylabel("Chi-square error", fontsize=30)
    plt.title("Error as a function of guessed C", fontsize = 36)
    plt.legend()
    plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
