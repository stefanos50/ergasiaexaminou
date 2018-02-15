import datetime
hmeres = ['Deutera','Trith','Tetarth','Pempth','Paraskeuh','Savvato','Kuriakh']
now = datetime.datetime.now()
hmeraonoma = now.weekday()
currxronos = now.year
currmhnas = now.month
currday = now.day
print "H shmerinh mera einai h",hmeres[hmeraonoma],now.strftime('%d-%m-%Y')
print "----------"
sum = 0
for i in range (currxronos+1 , currxronos+11):
	for j in range (1,13):
		hmka8emhna = datetime.date(i ,j,currday).weekday()
		if (hmka8emhna == hmeraonoma):
			sum = sum + 1
print "O arithmos apo thn mera",hmeres[hmeraonoma],"pou 8a uparxoun stis",currday,"tou mhna ta epomena 10 xronia einai:"
print sum