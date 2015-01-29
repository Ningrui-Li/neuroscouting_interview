from scipy import *
#from numpy import *
import matplotlib.pyplot as plt

sampling_rate = 500.0
Filt = array([58, 82])
time = arange(0, 5+1/sampling_rate, 1/sampling_rate)

freq1 = 60
freq2 = 35
freq3 = 10

signal = (1./3)*(sin(2*pi*freq1*time)+sin(2*pi*freq2*time)+sin(2*pi*freq3*time))
signal_FT = abs(fft(signal))

# create frequency x-axis labels for FT plot
L = (len(signal)-1)/2
f = arange(0, sampling_rate/2 + (sampling_rate/2)/L, (sampling_rate/2)/L)

# limit frequency range between 0 Hz - 75 Hz for FT plot
frequencyLimitIndices = nonzero(f<75);
f = f[frequencyLimitIndices];
signal_FT = signal_FT[frequencyLimitIndices];

# Unfiltered signal - time domain plot
plt.subplot(2, 1, 1)
plt.plot(time, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Unfiltered Signal (Sum of 10 Hz, 35 Hz, 60 Hz Sine Waves) - Time Domain')

# Unfiltered signal - frequency domain plot
plt.subplot(2, 1, 2)
plt.bar(f, signal_FT, width=0.2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Amplitude Spectrum of Unfiltered Signal - Frequency Domain')

plt.tight_layout()
plt.show()