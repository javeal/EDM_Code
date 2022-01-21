# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:11:13 2021

@author: Joe
"""

#import required libraries
import math
import matplotlib.pyplot as plt
import numpy as np
import wave
import pyaudio

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

#fig,ax =plt.subplots()
#ax.plot(time,sineWav,label='15kHz Tone')
#ax.set_title('numpy WAV data')
#ax.set_xlabel('Time (S)')
#ax.set_ylabel('Amplitude (V)?')
#ax.legend()
    
p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(2,unsigned = False),channels = 1,rate = sampRate,output = True)

#chunkSize = 1024
#
#for i in range(0,samples,chunkSize):
    
stream.write(sineWav)

stream.stop_stream()
stream.close()
    
p.terminate
    
    
    
    
    