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