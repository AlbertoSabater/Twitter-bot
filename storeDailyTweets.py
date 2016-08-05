#!/usr/bin/python

#EJECUTAR UNA VEZ AL PRINCIPIO DEL DIA

import os
import datetime
import time
import random
import tweepy
import sys


now = datetime.datetime.now()
name_file = str(os.path.dirname(os.path.abspath(__file__))) + '/data/' + str(now.month) + '/' + str(now.day) + '.txt'
with open(name_file) as f: 		# Get tweets for the current day
    lines = f.readlines()


hourIni = 9 		# Initial hour
hourEnd = 20 		# Final hour
interval = int((float(hourEnd-hourIni)/len(lines))*60)	# Interval between two regular posts in secs.
print "INTERVAL: " + str(interval)

wtime = datetime.datetime.now()
wtime = wtime.replace(hour=hourIni, minute=0, second=0, microsecond=0)
print str(wtime)

acumulated_time = 0

path = str(os.path.dirname(os.path.abspath(__file__))) + '/toWrite.txt'
f = open(path, 'w')

print "lines " + str(len(lines))

print("=============================================")

for i in range(0, len(lines)):			# For each post
	current_delay = random.randint(0,(i+1)*interval - acumulated_time)		# secs to sleep
	acumulated_time += current_delay
	add_delay = datetime.timedelta(minutes=current_delay)
	wtime = wtime + add_delay
	print str(wtime)
	print lines[i]

	f.write(str(wtime) + "\n")
	f.write(lines[i])
# end for

print("=============================================")

f.close()

