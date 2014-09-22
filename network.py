import random
import numpy as np 
from generate import *
from pprint import pprint
from misc import sigmoid, vvT

sigmoid_vec = np.vectorize(sigmoid)

class Network():
	def __init__(self,sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.weights = [np.ones((y,x))*0.3 for x,y in zip(sizes[:-1],sizes[1:])]
		print "weights=\n%s" % self.weights
		self.biases = [np.arange(y) for y in sizes[1:]]
		#self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])]
		#self.biases = [np.random.randn(y,1) for y in sizes[1:]]

	def apply(self,a_i,batch=False):

		if batch == False:
			a=np.array(a_i)

			for w,b in zip(self.weights,self.biases):
				a=sigmoid_vec(np.dot(w,a)+b)

		elif batch == True:
			a=[np.array(a_k) for a_k in a_i]
			for i in range(len(a)):
				for w,b in zip(self.weights,self.biases):
					a[i]=sigmoid_vec(np.dot(w,a[i])+b)

		return a

	def feed_forward(self,a_i):
		a=[np.array(a_i)]

		for w,b in zip(self.weights,self.biases):
			a.append(sigmoid_vec(np.dot(w,a[-1])+b))

		return a

	def backprop(self,x,y):
		delta=[]

		a_mat = self.feed_forward(x)
		delta.append(a_mat[-1]-y)

		for w,a in zip(self.weights[-1:0:-1],a_mat[-2:0:-1]):
			delta.append(np.dot(w.transpose(),delta[-1]))

		return delta[-1::-1], a_mat

	def bgd(self,training_set,eta):
		"""
		training_set must be a list of tuples (x,y)
		x is the input
		y is the desired output
		"""

		"""
		params is a list of tuples (delta,a_mat)
		each entry corresponds to a training example (x,y)
		"""
		params=[self.backprop(x,y) for x,y in training_set]	

		for i in xrange(self.num_layers-1):
			weights_update = np.zeros(self.weights[i].shape)
			biases_update = np.zeros(self.biases[i].shape)
			for delta, a_mat in params:
				weights_update += vvT(delta[i],a_mat[i])
				biases_update += delta[i]

			self.weights[i] = self.weights[i] - (eta/len(training_set))*weights_update
			self.biases[i] = self.biases[i] - (eta/len(training_set))*biases_update

	def sgd(self,training_set,eta,mini_batch_size=5):
		"""
		training_set must be a list of tuples (x,y)
		x is the input
		y is the desired output
		"""

		for k in range(len(training_set)/mini_batch_size):

			#	Pick mini_batch_size training examples from the training set
			mini_batch = [self.backprop(x,y) for x,y in training_set[k:k+mini_batch_size]]

			for i in xrange(self.num_layers-1):
				weights_update = np.zeros(self.weights[i].shape)
				biases_update = np.zeros(self.biases[i].shape)
				for delta, a_mat in mini_batch:
					weights_update += vvT(delta[i],a_mat[i])
					biases_update += delta[i]

				self.weights[i] = self.weights[i] - (eta/len(training_set))*weights_update
				self.biases[i] = self.biases[i] - (eta/len(training_set))*biases_update

		
