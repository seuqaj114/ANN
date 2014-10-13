import random

import numpy as np
from numpy.linalg import norm

def generate_random_set(size):
	t = 1.0
	random_set = [0]*size
	for i in range(size-1):
		prop = random.random()*t
		random_set[i] = prop
		t-=prop

	random_set[-1] = t

	return random_set

class Body():
	#	This class solves the problem of finding two matrices to solve the problem
	#	A1*A2 = E
	def __init__(self,desired,size1=(103680,3),size2=(3,8)):

		if type(desired).__name__ == "ndarray":
			self.E = desired
		else:
			self.E = np.array(desired)

		self.size1 = size1
		self.size2 = size2

		self.A1 = np.random.rand(*size1)
		self.A2 = np.random.rand(*size2)

		self.diff = norm(np.dot(self.A1,self.A2)-self.E)

		print self.A1.shape, self.A2.shape, self.E.shape

	def mutate(self,epochs=5):

		#	number of best solutions in a generation
		top = 3

		#	array2 is an array of tuples (matrix,error)
		array2 = []
		#	array2 lenght
		a2l = 40

		for i in range(a2l):
			temp_mat = np.random.rand(*self.size2)
			array2.append( (np.copy(temp_mat),self.cost(temp_mat)) )

		array2.sort(key=lambda x: x[1])
		print [item[1] for item in array2]

		for i in range(epochs):
			best = array2[:top]
			for j in range(top,(a2l-top)/2):
				random_set = generate_random_set(top)
				new_array = sum([array[0]*prop for array,prop in zip(array2,random_set)])
				array2[j] = (new_array,self.cost(new_array))
			for j in range((a2l-top)/2,a2l):
				new_array = np.random.rand(*self.size2)
				array2[j] = (new_array,self.cost(new_array))

			array2.sort(key=lambda x: x[1])
			print [item[1] for item in array2]

	def randomize(self,samples=10000):
		best_combo = []
		best_cost = self.diff
		for i in range(samples):
			new_a1 = np.random.rand(*self.size1)
			new_a2 = np.random.rand(*self.size2)
			if self.cost2(new_a1,new_a2) < best_cost:
				best_cost = self.cost2(new_a1,new_a2)
				best_array = np.copy([new_a1,new_a2])

				print best_cost

	def cost(self,array):
		return norm(np.dot(self.A1,array)-self.E)

	def cost2(self,a1,a2):
		return norm(np.dot(a1,a2)-self.E)