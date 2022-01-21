# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 09:06:56 2021

@author: Joe
"""

# import required libraries
import math
import matplotlib.pyplot as plt
import numpy as np
import wave
import pyaudio
from pynput import keyboard


# This function takes inputs from below and generates all waveforms
# assigned to keyboard ahead of time
def genWavTable(noteDict, keyDict, waveType, sampleRate):
    
    waveTable = {}
    
    for key in keyDict:
    
        note = keyDict[key]
        pitch = noteDict[note]
        period = 1/pitch
        
        typeMin = -1*math.pow(2,15)
        typeMax = math.pow(2,15)-1
        wavSampNum = math.floor(period/(1/sampleRate))
        wavPeriod = np.ndarray(shape = (wavSampNum),dtype = np.int16)
        time = np.linspace(0,period,wavSampNum)
        
        if waveType == "saw":
            m = int((typeMax-typeMin)/wavSampNum)
            for i in range(0,wavSampNum):
                wavPeriod[i] = typeMin+m*i
                
        elif waveType == "square":
            halfPeriod = math.floor(wavSampNum/2)
            for i in range(0,wavSampNum):
                if i < halfPeriod:
                    wavPeriod[i] = typeMin
                else:
                    wavPeriod[i] = typeMax
                    
        elif waveType == "triangle":
            halfPeriod = math.floor(wavSampNum/2)
            m = int((typeMax-typeMin)/halfPeriod)
            for i in range(0,wavSampNum):
                if i < halfPeriod:
                    wavPeriod[i] = typeMin+m*i
                else:
                    wavPeriod[i] = typeMax-m*(i-halfPeriod)
        elif waveType == "sine":    
            for i in range(0,wavSampNum):
                wavPeriod[i] = int(32767*math.sin(2*3.14159*pitch*time[i]))
        else:
            print("Pick a valid wave type")
            
        #waveTable[key] = np.matlib.repmat(wavPeriod,1,10)
        #waveTable[key] = wavPeriod
        waveTable[key] = np.tile(wavPeriod,100)

    return waveTable


# function handeling key presses
def on_press(key):
    try:
        keyVal = format(key.char)
    except AttributeError:
        keyVal = format(key)
        
    return keyVal


# function handeling key releases
# return a 1 to let loop know a key has been released
def on_release(key):
    return 1

def plotWaveTable(waveTable):
    for key in waveTable:
        waveform = waveTable[key]
        time = np.linspace(0,len(waveform),len(waveform))
        #plot single period of a wave
        fig,ax =plt.subplots()
        ax.plot(time,waveform,label='15kHz Tone')
        ax.set_title('numpy WAV data')
        ax.set_xlabel('Time (S)')
        ax.set_ylabel('Amplitude (V)?')
        ax.legend()



############################################################################
# Script begins here
############################################################################

sampleRate = 44100
samples = sampleRate*5


record = False;
freeRunning = False;

#create array that holds pitch of the waveforms
waveform = np.ndarray(shape = (samples), dtype = np.int16)

#select type of wave options are square, triangle, saw, sine
waveType = "saw"

keyToNote = {
        'j' : "a0",
        'k' : "b4",
        'l' : "c5"}


noteFrequencyTable = {
        "c0"  : 16.35,
        "cs0" : 17.32,
        "d0"  : 18.35,
        "ds0" : 19.45,
        "a0"  : 440,
        "b4"  : 493.88,
        "c5"  : 523.25}


waveTable = genWavTable(noteFrequencyTable, keyToNote, waveType, sampleRate)

plotWaveTable(waveTable)

p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(2,unsigned = False),channels = 1,rate = sampleRate,output = True)


#if freeRunning:
#    listener = pynput.keyboard.Listener(
#            on_press = on_press)
#else:
#    listener = pynput.keyboard.Listener(
#            on_press = on_press,
#            on_release = on_release)
    
    
keyVal = ''
release = 0
#listener.start()
# The event listener will be running in this block
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            break
        else:
            #print('Received event {}'.format(event))
            debugVal = event.key.char
            eventTracker = event
            stream.write(waveTable[debugVal])
    

stream.stop_stream()
stream.close()
    
p.terminate
    




