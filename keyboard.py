# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 23:30:14 2021

@author: Joe
"""

from pynput import keyboard

def on_press(key):
    try:
        print('Key Value key {0} pressed'.format(key.char))
        if key.char == 'q':
            return False
    except AttributeError:
        print('special Key {0}'.format(key))
        if format(key) == 'Key.esc':
            return False
        
    
        
        
#listener =  keyboard.Listener(
#        on_press = on_press)
#
#listener.start()
            
        
# The event listener will be running in this block
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            break
        else:
            print('Received event {}'.format(event))
        