#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os
import random
import lcddriver
import subprocess

display = lcddriver.lcd()

x = 1

while [x == 1 is True]:
	time.sleep(0.2)
	randomfile = random.choice(os.listdir('/home/pi/Music/')) #Random Music Script Start
	file = '/home/pi/Music/'+ randomfile
	print file
	display.lcd_clear()
	display.lcd_display_string(randomfile, 1)
	display.lcd_display_string('     Winning     ', 2)
	process = subprocess.Popen(['omxplayer', '-b', '-o', 'alsa:hw:1,0', file]) #Random Music Script End
	process.wait()
