from random import randint
from random import shuffle
import random 
def epilogespaixtwn(): 
	paixtes = []
	check = []
	for x in range (5):
		while True:
			z = randint(1,80)
			if z not in check:
				check.append(z)
				break
		paixtes.append(z)
	return paixtes
def epilogesupologisth(): 
	epiloges = []
	for i in range (1,81):
		epiloges.append(i)
	shuffle(epiloges)
	return epiloges
def oari8mosepiloghs(epiloges): 
	noumero = random.choice(epiloges)
	epiloges.remove(noumero);
	return noumero
def elegxosari8mwnpaixtwn(oloi,noumero):
	for i in range (0,len(oloi)):
		for j in range(0,len(oloi[i])):
			if oloi[i][j] == noumero:
				del oloi[i][j]
				break
	return oloi
def nikitis(oloi):
	for i in range (0,100):
		if not oloi[i]:
			return True
			break