import math, time, sys
import numpy as np

#returns whether the object at right ascension ra and declination dec is visible at local sidereal time lst
def rotation(ra, dec, lst):
    berklat = 37.8732 * math.pi/180
    berklong = -122.2573 * math.pi/180
    h = lst - ra
    #print h, berklat, dec, ra
    azimuth = math.atan(math.sin(h) / (math.cos(h) * math.sin(berklat) - math.tan(dec) * math.cos(berklat)))
    altitude = math.asin(math.sin(berklat) * math.sin(dec) + math.cos(berklat) * math.cos(dec) * math.cos(h))
    #print altitude
    if (altitude < 0 or altitude > math.pi / 2):
        return False
    return True

#returns an array. thingy is up between [0] and [1], looping over to 0 at 2pi
def whenisup(ra, dec):
    when = []
    for k in np.arange(0, 2 * math.pi, 0.0001):
        if (rotation(ra, dec, k)):
            when.append(k)
        else:
            when.append(12)
    if (len(when) > 0):
        return handle(when)
    print "Moron."

#dark magic
def handle(when):
    result = []
    twelve = (when[0] == 12)
    if not twelve:
        result.append(when[0])
    for k in range(0, len(when)):
        if ((not twelve) and when[k] == 12):
            twelve = True
            result.append(when[k-1])
        else:
            if (twelve and not(when[k] == 12)):
                twelve = False
                result.append(when[k])
    value = []
    if len(result) == 3:
        value.append(result[2])
        value.append(result[1])
        return value
    if len(result) == 1:
        result.append(2 * math.pi)
    return result

if __name__ == "__main__":
    print whenisup(float(sys.argv[1]), float(sys.argv[2]))
