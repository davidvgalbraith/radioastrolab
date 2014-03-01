import random
import math
import numpy as np
import matplotlib.pyplot as plt
#gets the mean of a uniform random sample of size n
def sample(n):
    mean = 0
    samp = []
    for k in range(0, n):
        point = random.uniform(-100.0, 100.0)
        mean += point
    mean /= n
    return mean

def centralimit():
    means = []
    for k in range(0, 1000000):
        means.append(sample(10))
    hist, bins = np.histogram(means, bins=50)
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align = 'center')
    plt.title("Means of samples of 10 Uniformly random numbers from -100 to 100", fontsize = 30)
    plt.xlabel("Mean", fontsize = 28)
    plt.ylabel("Frequency", fontsize = 28)
    plt.tick_params(axis='both', which='major', labelsize=24)

    plt.show()

def square(n):
    return n * n

#Gets the standard deviation of means of 100 random samples of size n 
#drawn from a Gaussian distribution of mean 0 and standard deviation 1
def stadev(n):
    samps=[]
    for q in range(0, 100):
        samp = []
        mu = 0
        for a in range(0, n):
            point = random.gauss(0, 1)
            mu += point
        samps.append(mu / n)
    var = 0
    moo = sum(samps) / 100
    for smp in samps:
        var += square(smp - moo)
    return math.sqrt(var)

def stdev():
    x = np.arange(1, 200, 1)
    y = [stadev(a) for a in x]
    z = [10/math.sqrt(b) for b in x]
    plt.plot(x, y, "ro")
    q, = plt.plot(x, z)
    plt.legend([q], ["10/sqrt(n)"])
    plt.title("Standard Deviations of Samples of Various Sizes", fontsize = 30)
    plt.xlabel("Sample size (n)", fontsize = 28)
    plt.ylabel("Standard Deviation", fontsize = 28)
    plt.tick_params(axis='both', which='major', labelsize=24)
    plt.show()

#divide array into subarrays of size, rounding off
def divide(array, size):
    ret = []
    while len(array) >= size:
        ret.append(array[0:size])
        array = array[size:]

    return ret

#Allan variance of the given array of measurements
def allanify(array):
    total = 0
    for x in range(1, len(array)):
        total += square(array[x] - array[x-1])
        
    return total / (2 * square(len(array)))
#"Allan variance test"
def allan():
    x = np.arange(1, 1001, 1)
    data = []
    allan = []
    for a in x:
        data.append(random.gauss(0, 1))
    for b in range(1, 501):
        groups = divide(data, b)
        means = [sum(group) / b for group in groups]
        allan.append(allanify(means))
    plt.plot(np.arange(1, 501), allan)
    plt.title("Allan Variance for Random Data", fontsize = 30)
    plt.xlabel("Partition size (n)", fontsize = 28)
    plt.ylabel("Allan Variance", fontsize = 28)
    plt.tick_params(axis='both', which='major', labelsize=24)
    plt.show()
#centralimit()
#stdev()

allan()
