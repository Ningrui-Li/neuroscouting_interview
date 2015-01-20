%% Neuroscouting, LLC
%% Exercise 
% (Requires SciPy and NumPy Libraries for Python)

%  Goal #1:
%   Use this MATLAB code to generate an analogous script in Python using 
%   SciPy and NumPy libraries. Generate a waveform, calculate its frequency
%   spectrum, and plot 1) the waveform over time and 2) the waveform's 
%   frequency sprecrum.


%  Goal #2:
%   In Python, use a bandstop filter to filter out the 60Hz signal in 
%   the waveform. Plot 1) the filtered waveform over time and 2) the 
%   filtered waveform's frequency spectrum. The 60Hz should now be removed. 

%   For your submission, we'd like to get a zipped git repository that includes the
%   code for the script (you can break it up in multiple files if you want to) along
%   with a README file that contains:
%   - Description of how the script works at a high-level
%   - How the code is organized (which modules do what, and their external dependencies)
%     and how control flows through the script.
%   - Interesting optimizations (if any)

clear all; close all;

%% Set initial conditions
sampling_rate = 500;                                % sampling rate
Filt = [58 62];                                     % bandstop filter range
time = 0:1/sampling_rate:5;                         % time

% set frequencies
freq1 = 60;                                         % create 60 Hz
freq2 = 35;
freq3 = 10;                                         

%% Generate signal based on set frequencies 
signal = ((sin(2*pi*freq1*time)+sin(2*pi*freq2*time)+sin(2*pi*freq3*time))/3);

%% Calculate frequency spectrum
signal_fft = abs(fft(signal));                      % fast fourier transform
L = (length(signal)-1)/2;                           % resolution
f=0:(sampling_rate/2)/L:(sampling_rate/2);          % index freqencies 

% index frequency below 75 Hz
index = find(f<75);
frequencies = f(index);
signal_fft = signal_fft(index);

%% Plot unfiltered signal and unfiltered frequency spectrum
figure
subplot(211)
plot(time,signal)
xlabel('Time (s)')
ylabel('Amplitude')
title('Unfiltered Signal')

subplot(212)
bar(frequencies,signal_fft)
title('Spectrum of Unfiltered Signal')
xlabel('frequency (Hz)')
ylabel('power')

