import matplotlib.pylab as plt
import numpy as np
import pylab
import scipy 
import scipy.signal
def deltanu(spectrum, freaks):
    deck = -1
    for k in np.arange(0, len(spectrum)):
        if (spectrum[k] == np.max(spectrum)):
            deck = k
    return abs(freaks[deck] - 1420.40575177)
#return an m by n gaussian array centered at (x, y) with standard deviations sigmax and sigmay and ampmlitude a
def getGaussian(m, n, x, y, sigmax, sigmay, a):
    gauss = np.zeros((m, n))
    for c in np.arange(0, m):
        q = c-x
        for d in np.arange(0, n):
            w = d-y
            gauss[c][d] += a * np.e ** (- ( (q)**2 / (2 * sigmax**2) + (w)**2 / (2 * sigmay**2)))
    return gauss
data = np.load('data.npz')
L = data['longitude'] ; B = data['latitude'] ; spec = data['spectrum'] ; freq = data['freqs']
print len(L)
hydrogens = []
m = np.zeros((1001, 1001))
for k in range(0, len(spec)):
    trum = spec[k]
    denu = deltanu(trum, freq) #megahertz
    distance = 400  #parsecs
    mh = 1.66e-24 #mass of hydrogen in grams
    omegab = 4 * np.pi/180 #beamwidth 4 dagrees
    ta = np.max(trum)
    hydrogen = 1.8e18 * denu * distance * distance * mh * ta * omegab
    x = (round(B[k]) + 70) * 1001/61
    y = (round(L[k]) - 160) * 1001/61
    velocity = -denu / 4.73
    m[x][y] = velocity
a = 1
for s in range(31, 32):
    size = 1001
    center = 500.5
    gauss = getGaussian(size, size, center, center, s, s, a)
    y = scipy.signal.fftconvolve(m, gauss, mode="same")
    #pylab.imshow(gauss)
    #pylab.show()
    pylab.imshow(y, extent=[160, 220, -70, -10], origin="lower", interpolation="nearest")
    pylab.colorbar()
    pylab.title("The superbubble: Our velocity measurements", fontsize=36)
    pylab.xlabel("Galactic Longitude", fontsize=30)
    pylab.ylabel("Galactic Latitude",fontsize=30)
    pylab.show()
