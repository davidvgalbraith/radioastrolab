import sys
import numpy as np
import matplotlib.pyplot as plt

def matrify(data, power):
    n = data.size
    X = []
    for a in range(0, power+1):
        X.append(data ** a)
    return np.transpose(np.matrix(X))

def polynomial(x, coeff):
    ret = 0
    for k in range(0, len(coeff)):
        ret += coeff[k] * x ** k
    return ret

def chisquare(arr):
    total = 0;
    for x in arr:
        total += x ** 2
    return total

def main(argv):
    data = np.load("ay121_lsq_data.npz")
    xvals = data["x"]
    xmatrix = matrify(xvals, int(argv[0]))
    xtrans = np.transpose(xmatrix)
    yvals = data["y"]
    atb = np.transpose(np.dot(xtrans, yvals))
    ata = np.dot(xtrans, xmatrix)
    x = np.linalg.solve(ata, atb)
    line = polynomial(xvals, x)
    residuals = abs(np.array(line)[0] - yvals)
    chi = chisquare(residuals)
    normchi = chi / (len(xvals) - int(argv[0]) - 1)
    print normchi
    plt.plot(xvals, np.array(line)[0], label="Best fit polynomial of degree " + argv[0])
    plt.plot(xvals, yvals, label="Measured data")
    plt.plot(xvals, residuals, label="Residuals")
    plt.legend()
    plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])
