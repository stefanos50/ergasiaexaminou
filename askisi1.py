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