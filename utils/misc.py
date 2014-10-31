import time
from random import random
import numpy as np

def countdown(seconds):
	print "Starting in %s" % seconds

	for i in range(seconds)[::-1]:
		time.sleep(1)
		print i

def generating_function(vec):
	return [sum(vec)/float(len(vec)),sum(vec)/float(len(vec))]
	#return [np.sin(vec[0])]

def generate(size,dim):
	def training_example(dim):
		t = [random() for j in range(dim)]
		return (t,generating_function(t))

	return [training_example(dim) for i in range(size)]

def conditional_np_array(a_i):
	if type(a_i).__name__ == "ndarray":
		return a_i
	elif type(a_i).__name__ == "list":
		return np.array(a_i)

def bubble_sort(l):
	unord = list(l)
	count = 0

	while(1):
		p = 0
		for i in range(1,len(unord)):
			if unord[i]<unord[i-1]:
				aux = unord[i-1]
				unord[i-1] = unord[i]
				unord[i] = aux
				p = 1
				count+=1
				#print unord

		if p == 0:
			break

	print "Operations till ordered: %s" % count

	return unord

def counting_sort(l):
	unord = list(l)

	store = [0]*256

	for value in unord:
		store[value] += 1

	ordered = []

	for i in range(len(store)):
		ordered += [i]*store[i]

	return ordered
