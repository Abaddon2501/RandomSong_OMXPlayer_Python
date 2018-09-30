#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #White Button

while True:
	time.sleep(0.1)
	input_state = GPIO.input(18) #White Button
	if input_state == False:
		print ('Next Song')
		time.sleep(0.2)
		os.system ('killall omxplayer.bin > /dev/null') #Kill OMXPlayer to play next song


