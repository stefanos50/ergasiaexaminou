#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler
import json
from collections import Counter
import re
import string
import os

def is_ascii(s):
    try:
        s.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False
tweetsli = [] 
def writetweetstoajsfile(tw,flname):
	with open(flname, 'w') as f:
		json.dump(tw._json, f)
		f.write('\n')

li1 = ['&amp;','/','?','@','$','%',';','^','&','*','_','-',':','.','!','#','"',"'",',','(',')']
def readtweetsfromjsfile(filename,k):
	if filename:
		with open(filename, 'r') as f:
			datastore = json.load(f)
	x = datastore['full_text'].encode('utf-8')
	x = re.sub(r'http\S+', '', x) #removing all the url's
	for i in range (0 , len(li1)):
		x = re.sub(u"(\xe2\x80\x99|\xe2\x80\x9c|\xe2\x80\x9d|έΑβ)", "", x) #removing escape characters
		x = x.replace(li1[i]," ") #removing punctuation that are in the list li1
	tweetsli.append(x.lower().split()) #split the words where is a space
	if k == 10:
		return tweetsli
def deletefileornot ():
	while True:
		print "Do you want to keep the json file with the data in your computer?"
		apantisi = int(raw_input("Press 1 if YES or 0 if NO:"));
		if apantisi == 0:
			os.remove(usern+'.json')
			break
		elif apantisi == 1:
			break

def nameexist(a):
	try:
		for status in tweepy.Cursor(api.user_timeline,screen_name=a,tweet_mode ='extended').items(1):
			print "" #if the profile does not exist this for loup will show an error
		return True
	except BaseException as e:
		return False
		
consumer_key ="YOUR-CONSUMER-KEY"
consumer_secret ="YOUR-CONSUMER-SECRET"
access_token ="YOUR-ACCESS-TOKEN"
access_secret ="YOUR-ACCESS-SECRET"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
while True:
	usern = raw_input("Give a twitter profil name without the @:");
	if nameexist(usern):
		break
	else:
		print "The twitter profile name does not exist please try again"
	
sum=0;
for status in tweepy.Cursor(api.user_timeline,screen_name=usern,tweet_mode ='extended').items():
	sum += 1 #Counting if the profile have at least 10 tweets in the profile
	if sum==10: #if the num is <10 then it will count only them 
		break;
for i in range (1,sum+1):
	for status in tweepy.Cursor(api.user_timeline,screen_name=usern,tweet_mode ='extended').items(i):
		writetweetstoajsfile(status,usern+'.json',)
	readtweetsfromjsfile(usern+'.json',i)
allwords = []
for i in range (0,sum):
	for j in range (0 , len(tweetsli[i])):
		if is_ascii(tweetsli[i][j]):
			if not tweetsli[i][j].isdigit():
				if len(tweetsli[i][j]) != 1:
					allwords.append(tweetsli[i][j])
metritis = Counter(allwords)
print metritis.most_common(1)
for value, count in metritis.most_common(1):
	print"The most famous word of the user is:",value
	print"Showed:",count,"times"
print"------------"
deletefileornot()