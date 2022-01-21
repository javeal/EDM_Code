# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:10:21 2021

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
samples = sampRate*3

timeMax = samples*sampPeriod
time = np.linspace(0,samples*sampPeriod,samples)

#create tone in numpy
sineWav = np.ndarray(shape=(samples),dtype = np.int16)
notes = np.array([261.63,1318.51,880,261.63,1318.51,880,261.63])
counts = np.array([int(sampRate*.5),int(sampRate*.5),int(sampRate*1),int(sampRate*.25),int(sampRate*.25),int(sampRate*.25),int(sampRate*.25)])
frequency = np.repeat(notes,counts) #in Hz

for i in range (0,sineWav.shape[0]-1):
    temp = int(32767*math.sin(2*3.14159*frequency[i]*time[i]))
    sineWav[i] = temp

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


