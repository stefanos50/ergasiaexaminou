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

plh8osephm = []
while True:
	flag = True
	x = raw_input("dwste 10  ari8mous me , anamesa tous :")	
	epiloges = x.split(",")
	if len(epiloges)==10:
		for i in xrange(10):
			epiloges[i]=int(epiloges[i])
		for i in range(0,8):
			for j in range(i+1,10):
				if epiloges[i] == epiloges[j]:
					flag = False
					print "oi ari8moi prepei na einai diaforetikoi"
					break
			if flag==False:
				break
		for i in range (0,10):
			if epiloges[i]>80 or epiloges[i]<1:
				flag = False
				print 'oi ari8moi prepei na einai apo to 1-80'
		if flag:
			break
	else:
		print 'oi ari8moi prepei na einai 10'

hmeres = ['Deutera','Trith','Tetarth','Pempth','Paraskeuh','Savvato','Kuriakh']
twrinhhmerom = datetime.datetime.now()
twrinhhmeromtel = datetime.datetime.now()
twrinhhmeromtel = twrinhhmeromtel - datetime.timedelta(days=1)