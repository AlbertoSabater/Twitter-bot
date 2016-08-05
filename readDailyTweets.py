#!/usr/bin/python

#EJECUTAR CADA VARIOS MINUTOS

import os
import datetime
import time
import random
import tweepy
import sys

# Consumer keys and access tokens, used for OAuth
from twitter_keys import consumer_key, consumer_secret, access_token, access_token_secret


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)


def postLongTweet ( tweet ) :
	try :
		tweet = tweet[:len(tweet)-1]
		j = 99
		while True:			# Split the text in two parts between two words
			if str(tweet[j]) == str(" "):
				firstString = tweet[:j]
				lastString = tweet[j:]
				break
			else :
				j = j+1

		lastWord = firstString.rsplit(None, 1)[-1]

		while lastWord[0].isupper() : 		# If the las word of the first part starts with uppercase, 
												#move that word to the second part
			j = j-1
			firstString = tweet[:j]
			lastString = tweet[j:]
			lastWord = firstString.rsplit(None, 1)[-1]

			if str(tweet[j]) == str(" ") and lastWord[0].isupper() :
				firstString = tweet[:j]
				lastString = tweet[j:]
				break

		firstString = firstString + " ..."
		lastString = "... " + lastString

		api.update_status(firstString)		# Post first tweet
		lastTweet = api.user_timeline(count = 1)[0]		# Get last tweet
		api.update_status(lastString, lastTweet.id)		# Reply last tweet
	except :
		print "Error while posting tweet"
### End of function


now = datetime.datetime.now()
#now = now.replace(hour=12, minute=38)


print  "----   " + str(now)

path = str(os.path.dirname(os.path.abspath(__file__))) + '/toWrite.txt'
f = open(path, 'r')
lines = f.readlines()
f.close()

count = 0
for i in range(0, len(lines),2):			# For each post
	date = datetime.datetime.strptime(lines[i].rstrip(), "%Y-%m-%d %H:%M:%S")

	if date <= now :

		try:
		  	api.update_status(lines[i+1].rstrip())			# Post tweet
		  	print "succes"
		except tweepy.TweepError as e:
			if e.message[0]['code'] == 186:		# In case of long tweet, call to funtion to split it
				print "Long tweet"
				postLongTweet(lines[i].rstrip())
		except:
			print "Unknown error\n"
			break


		print date
		print lines[i+1]
		count += 2
	else :
		break


if count > 0 :
	print "count > 0"
	path = str(os.path.dirname(os.path.abspath(__file__))) + '/toWrite.txt'
	print path
	open(path, 'w').writelines(lines[count:])





