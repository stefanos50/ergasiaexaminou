import urllib2
import json
import datetime

def euresiomoiwn(x,y):
	plh8os = 0
	plh8os2 = 0
	for i in range (0,10): 
		for j in range (0,20):
			if x[i] == y[j]:
				plh8os2 +=1
	if plh8os2 > 4:
		plh8os +=1
	return plh8os