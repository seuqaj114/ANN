import random
import numpy as np 
from generate import *
from pprint import pprint

# v1*v2T
def vvT(v1,v2):
	return v1.reshape((len(v1),1))*np.tile(v2,(len(v1),1))

def sigmoid(z):
	return 1.0/(1.0+np.exp(-z))

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

	def apply(self,a_i):
		a=np.array(a_i)

		#MUDAR ISTO PARA LIST COMPREHENSION
		for w,b in zip(self.weights,self.biases):
			a=sigmoid_vec(np.dot(w,a)+b)

		#print "output a=\n%s" % a
		return a

	def feed_forward(self,a_i):
		a=[np.array(a_i)]

		#MUDAR ISTO PARA LIST COMPREHENSION
		for w,b in zip(self.weights,self.biases):
			#print "w=\n%s\nb=\n%s" % (w,b)
			a.append(sigmoid_vec(np.dot(w,a[-1])+b))

		print "output a="
		pprint(a)
		print "desired = %s" % generating_function(a[0])
		return a

	def backprop(self,x,y):
		delta=[]

		a_mat = self.feed_forward(x)
		
		#delta.append((a_mat[-1]-y)*(a_mat[-1]*(1-a_mat[-1])))
		delta.append(a_mat[-1]-y)

		#MUDAR ISTO PARA LIST COMPREHENSION
		for w,a in zip(self.weights[-1:0:-1],a_mat[-2:0:-1]):
			#delta.append(np.dot(w.transpose(),delta[-1])*a)
			delta.append(np.dot(w.transpose(),delta[-1]))

		#print delta[-1::-1]
		return delta[-1::-1], a_mat

	def bgd(self,training_set,eta):
		"""
		training_set must be a list of tuples (x,y)
		x is the input
		y is the desired output
		"""

		params=[]
		"""
		params is a list of tuples (delta,a_mat)
		each entry corresponds to a training example (x,y)
		"""
		for x,y in training_set:
			#print self.backprop(x,y)
			params.append(self.backprop(x,y))


		for i in xrange(self.num_layers-1):
			weights_update = np.zeros(self.weights[i].shape)
			biases_update = np.zeros(self.biases[i].shape)
			for delta, a_mat in params:
				weights_update += vvT(delta[i],a_mat[i])
				biases_update += delta[i]

			self.weights[i] = self.weights[i] - (eta/len(training_set))*weights_update
			self.biases[i] = self.biases[i] - (eta/len(training_set))*biases_update

		#print "new weights=\n%s \nnew biases=\n%s" % (self.weights,self.biases)



"""
Training the OR function
"""
"""
training_set = [([1,0],[1]),([0,1],[1]),([0,0],[0]),([1,1],[1])]
net = Network([2,2,1])
for i in range(0,100):
	net.gd(training_set,5.0)
"""