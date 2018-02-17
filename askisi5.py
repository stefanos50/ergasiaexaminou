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
