#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os
import random
import lcddriver
import subprocess
from longstring import *

display = lcddriver.lcd()

x = 1

while [x == 1 is True]:
	time.sleep(0.2)
	randomfile = random.choice(os.listdir('/home/pi/Storage/Chelsea')) #Random Music Script Start
	file = '/home/pi/Storage/Chelsea/'+ randomfile
	print file
	display.lcd_clear()
	display.lcd_display_string("Chelsea's List", 2)
	process = subprocess.Popen(['omxplayer', '-b', '-o', 'alsa:hw:1,0', file]) #Random Music Script End
	while process.poll() == None:
		long_string(display, randomfile)
		time.sleep(0.1)
	else:
		print "Next Song"
		time.sleep(0.1)
