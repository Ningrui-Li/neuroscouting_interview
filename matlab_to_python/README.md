matlab_to_python
================
The assignment info can be found in `Neuroscouting_Exercise.m`

The analogous Python script is `neuroscouting_exercise_python.py`.
It can be run from the terminal by typing `python neuroscouting_exercise_python.py`

### Results
When the script is run, it will generate the following plots:

The first plot is of the magnitude response of the 60 Hz notch filter.

![60 Hz Notch Filter - Magnitude Response](https://raw.githubusercontent.com/Ningrui-Li/neuroscouting_interview/master/matlab_to_python/notch_filter.png)

The second plot contains the time domain and frequency domain magnitude plots of the unfiltered signal (containing 10 Hz, 35 Hz, and 60 Hz sinusoids)

![Unfiltered Signal](https://raw.githubusercontent.com/Ningrui-Li/neuroscouting_interview/master/matlab_to_python/unfiltered_signal.png)

The final plot shows the time domain and frequency domain magnitude plots of the signal after passing through the 60 Hz notch filter. As expected, the 60 Hz frequency component was filtered out.

![Filtered Signal](https://raw.githubusercontent.com/Ningrui-Li/neuroscouting_interview/master/matlab_to_python/filtered_signal.png)

### How it works
The 10 Hz, 35 Hz, and 60 Hz sum of sinusoids signal was created using the function `create_sine_wave`. The sampling rate of 500 Hz was defined in `sampling_rate`, the max time value of 5 seconds was defined in `maxTime`, and the frequencies in the signal were defined in the `frequencies` array.

Next, the signal was passed into the function `notch_filter_signal`, which returned the signal after being passed through a notch filter. The notch filter passband frequencies (in Hz) were defined as 58 Hz and 62 Hz in `Wp`. The stopband frequencies (in Hz) were defined as 59 Hz and 61 Hz in `Ws`. `notch_filter_signal` used functions in the SciPy signal processing library to create a Butterworth filter with those passband and stopband frequencies. The maximum passband ripple was assumed to be -3 dB, and the minimum stopband attenuation was assumed to be -40 dB. Finally, there is an optional input argument to `notch_filter_signal` that will create a plot of the magnitude response of the filter for debugging purposes.

Plots of the filtered and unfiltered signals in the time and frequency domains were created using the function `create_time_freq_plots`. The range of displayed frequencies was limited to be between 0 and 75 Hz since the highest frequency component in the signal was 60 Hz.