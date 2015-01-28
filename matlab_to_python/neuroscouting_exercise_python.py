from numpy import *
import scipy

sampling_rate = 500.0
Filt = array([58, 82])
time = arange(0, 5+1/sampling_rate, 1/sampling_rate)

freq1 = 60
freq2 = 35
freq3 = 10

signal = (1./3)*(sin(2*pi*freq1*time)+sin(2*pi*freq2*time)+sin(2*pi*freq3*time))
