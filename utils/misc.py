import time
from random import random
import numpy as np

def countdown(seconds):
	print "Starting in %s" % seconds

	for i in range(seconds)[::-1]:
		time.sleep(1)
		print i

def generating_function(vec):
	return [sum(vec)/float(len(vec))]
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