from random import random
import numpy as np

def generating_function(vec):
	return [sum(vec)/float(len(vec))]
	#return [np.sin(vec[0])]

def generate(size,dim):
	def training_example(dim):
		t = [random() for j in range(dim)]
		return (t,generating_function(t))

	return [training_example(dim) for i in range(size)]