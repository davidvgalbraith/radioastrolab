import numpy as np
import matplotlib.pyplot as plt

b = [-70., -68., -66., -64., -62., -60., -58., -56., -54., -52., -50.,
       -48., -46., -44., -42., -40., -38., -36., -34., -32., -30., -28.,
       -26., -24., -22., -20., -18., -16., -14., -12., -10.]

for i in b:
    File = np.load('Points/'+str(i)+'.npz') # Loading File
    x = File['x']
    y = File['y']
    pos = 0
    for value in y:
        if value == 1:
            plt.plot(x[pos], i, 'ro')
            pos = pos + 1
        if value == 0:
            plt.plot(x[pos], i, 'bo')
            pos = pos + 1
        if value == 2:
            plt.plot(x[pos], i, 'go')
            pos = pos + 1
#plt.legend()
plt.axis([155,225,-75,-5])
plt.title('Points Checked by Telescope', size = 22)
plt.xlabel(r'Galactic Longitude' + '  $l$', size = 20)
plt.ylabel(r'Galactic Latitude' + '  $b$', size = 20)
plt.show()


