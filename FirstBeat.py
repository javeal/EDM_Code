# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:06:11 2021

@author: Joe
"""

#import required libraries
import math
import matplotlib.pyplot as plt
import numpy as np
import wave
#import scipy

# sample rate of .wav file
sampRate = 44100 # Hz
sampPeriod = 1/sampRate
# samples for tone
samples = sampRate*10

timeMax = samples*sampPeriod
time = np.linspace(0,samples*sampPeriod,samples)

#create tone in numpy
sineWav = np.ndarray(shape=(samples),dtype=np.int16)
frequency = 20.6 #in Hz
beatfreq = frequency+1;

for i in range (0,sineWav.shape[0]-1):
    beatVal = math.sin(2*3.14159*frequency*time[i]) +  math.sin(2*3.14159*beatfreq*time[i])
    sineWav[i] = int(32767*beatVal)

fig,ax =plt.subplots()
ax.plot(time,sineWav,label='120 Hz Beat Tone')
ax.set_title('numpy WAV data')
ax.set_xlabel('Time (S)')
ax.set_ylabel('Amplitude (V)?')
ax.legend()

#save as .wav file
fileName = "fireCracker.wav"

toneWav = wave.open(fileName,"w")

toneWav.setnchannels(1)
toneWav.setframerate(sampRate)
toneWav.setnframes(samples)
toneWav.setsampwidth(2)

toneWav.writeframes(sineWav)

toneWav.close()                                                                                                                                                                                                                                                                                                           


