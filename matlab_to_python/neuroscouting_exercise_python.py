from scipy import *
from scipy import signal as sig
import matplotlib.pyplot as plt
    
def main():    
    sampling_rate = 500.0
    maxTime = 5
    frequencies = [10, 35, 60]
    time, signal = create_sine_wave(sampling_rate, maxTime, frequencies)

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

    # Make 60 Hz Notch Filter Magnitude Response plot
    w_notch_filt, H_notch_filt = sig.freqz(B, A)
    w_notch_filter = multiply(w_notch_filt, (sampling_rate/2)/pi) # convert from radians to Hz

    plt.figure(1)
    plt.plot(w_notch_filter, abs(H_notch_filt))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Notch Filter Amplitude')
    plt.title('60 Hz Notch Filter - Magnitude Response')

    # Apply notch filter to signal -> also get FFT of filtered signal
    signal_filtered = sig.filtfilt(B, A, signal)
    signal_filtered_FT = abs(fft(signal_filtered))

    # limit frequency range between 0 Hz - 75 Hz for FT plot
    frequencyLimitIndices = nonzero(f<75);
    f = f[frequencyLimitIndices]
    signal_FT = signal_FT[frequencyLimitIndices]
    signal_filtered_FT = signal_filtered_FT[frequencyLimitIndices]

    # Unfiltered signal time and freq plots
    create_time_freq_plots(time, signal, f, signal_FT,
                           'Unfiltered Signal')

    # 60 Hz notch filtered signal time and freq plots
    create_time_freq_plots(time, signal_filtered, f, signal_filtered_FT,
                           '60 Hz Notch Filtered Signal')

    plt.tight_layout()
    plt.show()

def create_sine_wave(fs, maxTime, freqs):
    '''
    This function creates a signal consisting of a sum of sinusoids
    with frequencies defined in freqs and amplitude 1.
        
    Inputs:
    fs - sampling rate (Hz)
    maxTime - Maximum time (s) to which signal is calculated.
    freqs - Array of sine frequencies (Hz) to include.

    Outputs:
    time - time vector of signal (s)
    signal - signal amplitude through time
    
    Ex: 
    Create signal with sampling rate 500 Hz, with sine waves of
    frequences 60 Hz, 30 Hz, and 15 Hz. Evaluate from 0 s to 5 s.
    
    time, signal = create_sine_wave(500, 5, [60 30 15])
    '''
    time = arange(0, maxTime+1/fs, 1/fs)
    signal = empty(len(time), dtype=float) 
    for freq in freqs:
        signal += sin(2*pi*freq*time)
        
    signal = signal / len(freqs) # Scale to unity amplitude
    return time, signal
    
def create_time_freq_plots(time, signal_time, freq, signal_FT, title):
    '''
    This function creates a figure with two subplots showing the
    time and frequency domain plots of the given signal vectors.
    Assumes time is in seconds and frequency is in Hz.
    '''
    plt.figure()
    # time domain plot
    plt.subplot(2, 1, 1)
    plt.plot(time, signal_time)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(title + '- Time Domain')

    # frequency domain plot
    plt.subplot(2, 1, 2)
    plt.bar(freq, abs(signal_FT), width=0.2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power')
    plt.title(title + ' - Frequency Domain')
    
main()