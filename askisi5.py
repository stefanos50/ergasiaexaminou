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