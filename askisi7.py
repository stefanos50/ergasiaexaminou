import datetime
hmeres = ['Deutera','Trith','Tetarth','Pempth','Paraskeuh','Savvato','Kuriakh']
now = datetime.datetime.now()
hmeraonoma = now.weekday()
currxronos = now.year
currmhnas = now.month
currday = now.day
print "H shmerinh mera einai h",hmeres[hmeraonoma],now.strftime('%d-%m-%Y')
print "----------"