# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:56:16 2021

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
Cfreq = 261.63 #in Hz
Efreq = 329.63
Gfreq = 392

for i in range (0,sineWav.shape[0]-1):
    chordVal = math.sin(2*3.14159*Cfreq*time[i]) +  math.sin(2*3.14159*Efreq*time[i]) +  math.sin(2*3.14159*Gfreq*time[i])
    sineWav[i] = int(32767*chordVal)

fig,ax =plt.subplots()
ax.plot(time,sineWav,label='15kHz Tone')
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


