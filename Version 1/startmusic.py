#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Green Button

while True:
        time.sleep(0.1)
        input_state = GPIO.input(21) #Green Button
        if input_state == False:
                print ('Start Music') #Print to Shell
                time.sleep(0.2)
                os.system ('/home/pi/lcd/./whilex.py') #Start the Infinite Loop
