#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Blue Button

while True:
        time.sleep(0.1)
        input_state = GPIO.input(7) #Blue Button
        if input_state == False:
                print ('Start Music') #Print to Shell
                time.sleep(0.2)
                #process = subprocess.Popen('/home/pi/lcd./startmusic.py')
                #process1 = subprocess.Popen('/home/pi/lcd./stopmusic.py')
		#os.system ('/home/pi/lcd/./stopmusic.pu') #Start the Infinite Loop
		#os.system ('/home/pi/lcd/./killomx.py')
		os.system ('/home/pi/lcd/./chelsealoop.py')
