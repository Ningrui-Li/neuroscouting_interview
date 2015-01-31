from scipy import *
from scipy import signal as sig
#from numpy import *
import matplotlib.pyplot as plt

sampling_rate = 500.0
time = arange(0, 5+1/sampling_rate, 1/sampling_rate)

freq1 = 60
freq2 = 35
freq3 = 10

signal = (1./3)*(sin(2*pi*freq1*time)+sin(2*pi*freq2*time)+sin(2*pi*freq3*time))
signal_FT = abs(fft(signal))

## create frequency x-axis labels for FT plot
L = (len(signal)-1)/2
f = arange(0, sampling_rate/2 + (sampling_rate/2)/L, (sampling_rate/2)/L)

## create 60 Hz notch filter
Wp = [58, 62]                        # Passband edge frequencies (Hz)
Ws = [59, 61]                        # Stopband edge frequencies (Hz)
Wp = divide(Wp, sampling_rate/2)     # Normalize to radians
Ws = divide(Ws, sampling_rate/2)

# Get Butter filter parameters and create bandstop filter using those params
N, Wn = sig.buttord(Wp, Ws, 3, 40)  # N = order of Butterworth filter
                                    # Wn = Butterworth cutoff frequencies
B, A = sig.butter(N, Wn, 'stop')

# Check 60 Hz Notch Filter Frequency Response
w_notch_filt, H_notch_filt = sig.freqz(B, A)
w_notch_filter = multiply(w_notch_filt, (sampling_rate/2)/pi) # convert from radians to Hz

plt.figure(1)
plt.plot(w_notch_filter, abs(H_notch_filt))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Notch Filter Amplitude')
plt.title('60 Hz Notch Filter - Magnitude Response')

# limit frequency range between 0 Hz - 75 Hz for FT plot
frequencyLimitIndices = nonzero(f<75);
f = f[frequencyLimitIndices];
signal_FT = signal_FT[frequencyLimitIndices];

# Unfiltered signal - time domain plot
plt.figure(2)
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