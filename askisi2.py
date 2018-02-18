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

def isthereanychar(epil):
	try:
		for i in range (10):
			int(epiloges[i])
		return True
	except ValueError:
		return False

plh8osephm = []
while True:
	flag = True
	x = raw_input("dwste 10  ari8mous me , anamesa tous :")	
	epiloges = x.split(",")
	if len(epiloges)==10:
		flag2 = isthereanychar(epiloges)
		for i in xrange(10):
			if flag2 == True:
				epiloges[i]=int(epiloges[i])
		for i in range(0,8):
			if flag2 == False:
				break
			for j in range(i+1,10):
				if epiloges[i] == epiloges[j]:
					flag = False
					print "oi ari8moi prepei na einai diaforetikoi"
					break
			if flag==False:
				break
		for i in range (0,10):
			if flag2 == False:
				break
			if epiloges[i]>80 or epiloges[i]<1:
				flag = False
				print 'oi ari8moi prepei na einai apo to 1-80'
				break
		if not flag2:
			print "prepei na periexontai mono ari8moi kai oxi xarakthres h keno"
		if flag and flag2:
			break
	else:
		print 'oi ari8moi prepei na einai 10'

hmeres = ['Deutera','Trith','Tetarth','Pempth','Paraskeuh','Savvato','Kuriakh']
twrinhhmerom = datetime.datetime.now()
twrinhhmeromtel = datetime.datetime.now()
twrinhhmeromtel = twrinhhmeromtel - datetime.timedelta(days=1)

for i in range (31):
	twrinhhmerom = twrinhhmerom - datetime.timedelta(days=1)
	date_format= twrinhhmerom.strftime("%d-%m-%Y")
	url = 'http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_format
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	data = json.loads(data)
	klhrwseis = data['draws']['draw']
	telikoplh8os = 0
	for i in klhrwseis:
		temp = i["results"]
		telikoplh8os += euresiomoiwn(epiloges,temp)
	plh8osephm.append(telikoplh8os) #h lista periexei ton ari8mo epituxiwn gia ka8e mera
max = max(plh8osephm)
for i in range (len(plh8osephm)): 
	if plh8osephm[i] == max:
		teliki = twrinhhmeromtel - datetime.timedelta(days=i) 
		print "H h mera tou mhna me tis perissoteres epituxies einai:"
		print hmeres[teliki.weekday()],teliki.strftime('%d-%m-%Y')