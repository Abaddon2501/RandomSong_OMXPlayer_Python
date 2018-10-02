#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os
import lcddriver

display = lcddriver.lcd()

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Red Button

while True:
	time.sleep(0.1)
	input_state = GPIO.input(12) #Red Button
	if input_state == False:
		print ('Music Stopped')
		time.sleep(0.2)
		display.lcd_clear()
		display.lcd_display_string('      Music      ', 1)
		display.lcd_display_string('     stopped     ', 2)
		os.system ('killall omxplayer.bin > /dev/null') #Kill OMXPlayer
		os.system ('pkill -9 -f ./whilex.py') #Kill Infinite Loop Script
		os.system ('pkill -9 -f ./chelsealoop.py') #Kill Infinite Loop Script
		os.system ('pkill -9 -f ./scrollx.py') #Kill infinite Loop Script
