#!/usr/bin/env python

#@author Kyle Moses
import numpy as np
import matplotlib.pyplot as plt
import readspec_mod as rsm
import os
import scipy.constants as spc

def boxavg(data, radius=10):                                              
    new = np.zeros(data.shape)
    for i in np.arange(radius, len(data)-radius+1):
        new[i] = np.median(data[i-radius:i+radius])
    return new  


b = [-70., -68., -66., -64., -62., -60., -58., -56., -54., -52., -50.,
       -48., -46., -44., -42., -40., -38., -36., -34., -32., -30., -28.,
       -26., -24., -22., -20., -18., -16., -14., -12., -10.]
        
stuff = np.load('calibrated/data.npz')
longitude = stuff['longitude']
latitude = stuff['latitude']
data = stuff['spectrum']
                                                        
for i in b:
    File = np.load('Points/'+str(i)+'.npz')
    longpts = File['x']
    for n in longpts:
        
	index = 0 ; havepoint = False
	for lat in latitude:
	    if lat == i:
		if longitude[index] == n:
		    havepoint = True
		    break	
	    index += 1
	if havepoint:
	    continue

        if not os.path.isfile('raw/specOFF/bubbleOFF'+str(n)+','+str(i)+'0.log'):                       
            continue
        if not os.path.isfile('raw/specON/bubbleON'+str(n)+','+str(i)+'0.log'):                                            
            continue


        if not os.path.isfile('raw/noiseOFF/bubbleNOISE_OFF'+str(n)+','+str(i)+'0.log'):                            
            continue
        if not os.path.isfile('raw/noiseON/bubbleNOISE_ON'+str(n)+','+str(i)+'0.log'):                                       
            continue
	spec_off = rsm.readSpec('raw/specOFF/bubbleOFF'+str(n)+','+str(i)+'0.log')                                                            
        spec_off = boxavg(np.mean(spec_off,1))           

        spec_on = rsm.readSpec('raw/specON/bubbleON'+str(n)+','+str(i)+'0.log')                                                                        
        spec_on = boxavg(np.mean(spec_on,1))

        noise_off = rsm.readSpec('raw/noiseOFF/bubbleNOISE_OFF'+str(n)+','+str(i)+'0.log')                                                      
        noise_off = boxavg(np.mean(noise_off,1))    

        noise_on = rsm.readSpec('raw/noiseON/bubbleNOISE_ON'+str(n)+','+str(i)+'0.log')                                                
        noise_on = boxavg(np.mean(noise_on,1))                     

        fc = 1272.4+150
        f_range = np.linspace(fc-6, fc+6, spec_off.shape[0])

        plt.plot(f_range, spec_off, label = "Spec off")
        plt.plot(f_range, spec_on, label = "Spec on")
        plt.plot(f_range, noise_off, label= "Noise off")
        plt.plot(f_range, noise_on, label= "Noise on")
        plt.title("All measurements for " + '(' + str(n) + ', ' + str(i) + ')', fontsize=44)
        plt.tick_params(axis='both', which='major', labelsize=28)
        plt.xlabel('MHz', fontsize=32)
        plt.ylabel('Signal', fontsize=32)
        plt.legend()
        plt.show()


        #P_on = np.sum(noise_on - spec_on)/100. 
        #t_sys_on = np.sum(spec_on)/P_on
        #P_off = np.sum(noise_off - spec_off)/100.
        #t_sys_off = np.sum(spec_off)/P_off                                    
        T_noise = 100
        Y_on = np.sum(noise_on)/np.sum(spec_on)
        t_sys_on = T_noise/(Y_on-1)
        Y_off = np.sum(noise_off)/np.sum(spec_off)
        t_sys_off = T_noise/(Y_off-1)

        G_ratio = (np.sum(spec_on)/np.sum(spec_off))

        spec_off = spec_off * G_ratio
        noise_off = noise_off * G_ratio


        cal_on = ((spec_on[(2731-1365):(2731+1366)]/spec_off[(2731-1365):(2731+
        1366)])-1) * t_sys_on
        cal_off = ((spec_off[(5461-1365):(5461+1366)]/spec_on[(5461-1365):(5461
        +1366)])-1) * t_sys_off *(t_sys_on/t_sys_off)
        new_f_range = np.linspace(1420.4-2,1420.4+2,1365*2+1)

#Fitting a polynomial to the data
        coeff_on = np.polyfit(np.delete(new_f_range, np.s_[1280:-1280]), np.delete(cal_on,np.s_[1280:-1280]), 5)
        coeff_off = np.polyfit(np.delete(new_f_range, np.s_[1280:-1280]), np.delete(cal_off,np.s_[1280:-1280]), 5)
        fit_on = (coeff_on[0] * new_f_range**5) + (coeff_on[1]*new_f_range**4) + (coeff_on[2]*new_f_range**3) + (coeff_on[3]*new_f_range**2) + (coeff_on[4]*new_f_range) + (coeff_on[5])
        fit_off = (coeff_off[0] * new_f_range**5) + (coeff_off[1]*new_f_range**4) + (coeff_off[2]*new_f_range**3) + (coeff_off[3]*new_f_range**2) + (coeff_off[4]*new_f_range) + (coeff_off[5])


        cal_on = cal_on - fit_on
        cal_off = cal_off - fit_off
        cal = (cal_on + cal_off)/2.

	
        plt.plot(new_f_range, cal)
        plt.ylabel('Temperature (K)', fontsize=20)
        plt.xlabel('Frequency (MHz)', fontsize=20)
        plt.title('(' + str(n) + ', ' + str(i) + ')')
	#plt.plot(new_f_range, cal_on)                                         
        #plt.plot(new_f_range, cal_off)                                        
        #plt.show()
	
	#q = raw_input('Save Data? (y/n): ')
	if 47 == 'y':
		longitude = np.append(longitude, n)
		latitude = np.append(latitude, i)
		data = np.append(data, cal)
		data = data.reshape(data.size/cal.size, cal.size)
	

                np.savez('calibrated/data.npz', longitude = longitude, latitude = latitude, spectrum = data, freqs = new_f_range)
