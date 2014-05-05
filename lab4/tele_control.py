import numpy as np
import ephem
import time
import radiolab as rlab
import dish
import dish_synth
import rot_func
import takespec
#import readspec.mod

################################
## Recording and loading data ##

alt_lim = np.loadtxt('alt_limits_2.txt') # Limits of Alt that I can't reach
az_lm = np.arange(0., 361., 1.) # correspondent azimuths

##########

##################################
#interpolating the pointing limits
#interpolation = np.array([])
def interp(az):
#for az in AZ*180/np.pi:
    interpolation = (alt_lim[int(az)]*(1 - (az - int(az))) + alt_lim[int(az) + 1]*(az - int(az))) 
    return interpolation
##########

#########################
## Telescope Functions ##

# To Track
d = dish.Dish() # From dish module
baseFreq = 1272.4 # In MHz
s = dish_synth.Synth()
s.set_amp(10)

# Setting Points
b = np.arange(-70.,-10, 2.) # galactic latitudes
b = np.append(b, -10.)

n = input('Time to stop (24 hours format): ')

# Pointing Home to begin observation 
print 'Home! - at ' +  str(time.localtime()[3]) + ':' + str(time.localtime()[4])
#d.home()
print 'Done homing!'
print

date = str(time.localtime()[1]) + '-' + str(time.localtime()[2]) + '-' + str(time.localtime()[3]) + ':' + str(time.localtime()[4])

log = open('Logs/obs_log_'+str(date), 'w')
log.write('Observation starts at ' + str(time.localtime()[3]) +':'+str(time.localtime()[4]) +':'+str(time.localtime()[5])+'\n')

log.write('Homing at' +  str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + '\n')
log.write('ALT ' + 'AZ ' + 'TIME' + '\n')

while time.localtime()[3] != n:

    for i in b:
        if time.localtime()[3] == n: break

        File = np.load('Points/'+str(i)+'.npz') # Loading File
        long_points = File['x'] # Longitude Points
        conf = File['y'] # Chcking Points (0 or 1)
        obs_time = File['z'] # Observation window

        for j in long_points: # For each galactic longitude values (j)
            if time.localtime()[3] == n: break

            isup = obs_time[list(long_points).index(j)] # Start and End time for this longitude

            lst_now =  rlab.getLST() # Local Sidereal Time 

            if isup[0] < isup[1]: 
                if isup[0] < lst_now < isup[1]:
                    track = 1 # Able to point
                else:
                    track = 0 # Unable

            else:
                if isup[0] < lst_now < 24 or 0 < lst_now < isup[1]:
                    track = 1 # Able to point
                else:
                    track = 0 # Unable

            if track == 1: # Checking, via z column, if I can point 
        
                if conf[list(long_points).index(j)] == 0.: # Checking, via y column, if I already pointed

                    alt, az = rot_func.convert(j,i)[0], rot_func.convert(j,i)[1] # Defining alt, az

                    print 'Tracking ', 'alt-'+ str(alt), 'az-' + str(az)
        
                    log.write(str(j) + ' ' + str(i) + ' - ' + 'gal_long / gal_lat' + '\n')
                    log.write(str(alt) + ' ' + str(az) + ' ' + str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + '\n')

                    
                    while True:
                        try:
                            d.noise_off()  
                            break
                        except:
                            print 'Noise set failed... trying again'
                    
                    
                    s.set_freq(baseFreq)
                    s.set_amp(10)

                    try:
                        d.point(alt, az)
                    except (ValueError):
                        print 'ValueError returned, moving to next point!'
                        continue

                    takespec.takeSpec('specON/bubbleON' + str(j) + ','+ str(i), numSpec = 128)

                    print
                    print 'Spectra taken!'

                    while True:
                        try:
                            d.noise_on()
                            break
                        except:
                            print 'Noise set failed... trying again'

                    d.point(alt, az)
                    takespec.takeSpec('noiseON/bubbleNOISE_ON' + str(j) + ',' + str(i), numSpec = 32)
                    print
                    print 'Noise taken!'

                    while True:
                        try:
                            d.noise_off()  
                            break
                        except:
                            print 'Noise set failed... trying again'

                    s.set_freq(baseFreq - 4)
                    s.set_amp(10)
                    d.point(alt, az)
                    takespec.takeSpec('specOFF/bubbleOFF' + str(j) + ',' + str(i), numSpec = 128)

                    print
                    print 'Spectra Off taken!'

                    while True:
                        try:
                            d.noise_on()
                            break
                        except:
                            print 'Noise set failed... trying again'

                    d.point(alt, az)
                    takespec.takeSpec('noiseOFF/bubbleNOISE_OFF' + str(j) + ',' + str(i), numSpec = 32)
                    print
                    print 'Noise Spec_Off taken!'

                    while True:
                        try:
                            d.noise_off()  
                            break
                        except:
                            print 'Noise set failed... trying again'

                    print 'Done! Writing 1 on File.'
                    print
                    conf[list(long_points).index(j)] = 1. # Writing 1 on y axis
                    np.savez('Points/'+str(i), x = long_points, y = conf, z = obs_time) # Resaving axis

                else:
                    #time.sleep(2)
                    print
                    print 'Already pointed there - 1 found', str(i) + ' - ' + str(j), ' / ' +  str(lst_now) + ' - ' + str(isup)
            
            else:
                #time.sleep(2)
                print 'Point not observable now - moving to next point', str(i) + ' - ' + str(j), ' / ' +  str(lst_now) + ' - ' + str(isup)

log.close()
##########


