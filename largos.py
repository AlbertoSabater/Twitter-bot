#!/usr/bin/python

import os
import datetime
import time
import random
import tweepy
import sys


name_file = str(os.path.dirname(os.path.abspath(__file__))) + '/largos.txt'

with open(name_file) as f:
    lines = f.readlines()


for i in range(0, len(lines)):			# For each post

	lines[i] = lines[i][:len(lines[i])-1]
	j = 99
	while True:
		if str(lines[i][j]) == str(" "):
			firstString = lines[i][:j]
			lastString = lines[i][j:]
			break
		else :
			j = j+1

	lastWord = firstString.rsplit(None, 1)[-1]

	while lastWord[0].isupper() : 
		j = j-1
		firstString = lines[i][:j]
		lastString = lines[i][j:]
		lastWord = firstString.rsplit(None, 1)[-1]

		if str(lines[i][j]) == str(" ") and lastWord[0].isupper() :
			firstString = lines[i][:j]
			lastString = lines[i][j:]
			break

	print "1. " + firstString + " " + "(...)"
	#print "3. " + firstString.rsplit(None, 1)[-1]
	print "2. " + lastString + " " + "(...)"
