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