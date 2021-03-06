from random import random
import numpy as np 
from pprint import pprint
from utils.math import sigmoid, vvT
from numpy.linalg import norm

sigmoid_vec = np.vectorize(sigmoid)
tanh_vec = np.vectorize(np.tanh)
#sigmoid_vec = np.vectorize(sig)

class Network():
	def __init__(self,sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes

		#self.biases=[np.array([-90, -40]), np.array([-30.0])]
		#self.weights= [np.array([[ 60.0,  60.0],[ 80.0,  80.0]]), np.array([[ -60.0, 60.0  ]])]

		#self.weights = [np.ones((y,x))*50.0 for x,y in zip(sizes[:-1],sizes[1:])]
		self.biases = [np.array([random() for i in range(y)]) for y in sizes[1:]]
		self.weights = [(np.random.rand(y,x)) for x,y in zip(sizes[:-1],sizes[1:])]
		#self.biases = [np.random.randn(y,1) for y in sizes[1:]]

	def apply(self,a_i,batch=False):

		if batch == False:

			a=np.array(a_i)

			for w,b in zip(self.weights,self.biases):
				#print w.shape, a.shape,b.shape
				a=sigmoid_vec(np.dot(w,a)+b)

		elif batch == True:
			a=[np.array(a_k) for a_k in a_i]
			for i in range(len(a)):
				for w,b in zip(self.weights,self.biases):
					a[i]=sigmoid_vec(np.dot(w,a[i])+b)

		return a

	def feed_forward(self,a_i):
		a_mat=[np.array(a_i)]

		for w,b in zip(self.weights,self.biases):
			#print w.shape, a_mat[-1].shape, b.shape
			a_mat.append(sigmoid_vec(np.dot(w,a_mat[-1])+b))

		return a_mat

	def backprop(self,x,y):
		delta=[]

		a_mat = self.feed_forward(x)
		delta.append(a_mat[-1]-y)

		for w,a in zip(self.weights[-1:0:-1],a_mat[-2:0:-1]):
			#delta.append(np.dot(w.transpose(),delta[-1])*a*(1-a))
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
		backprop_params=[self.backprop(x,y) for x,y in training_set]	
		#pprint(backprop_params[0][0][0])

		for i in xrange(self.num_layers-1):
			weights_update = np.zeros(self.weights[i].shape)
			biases_update = np.zeros(self.biases[i].shape)
			for delta, a_mat in backprop_params:
				weights_update += vvT(delta[i],a_mat[i])
				#print "delta[%s] %s" % (i,delta[i])
				#print "a_mat[%s] %s" % (i,a_mat[i])
				#print "vvT[%s] %s" % (i,vvT(delta[i],a_mat[i]))
				biases_update += delta[i]


			#print "weights %s" % weights_update
			#print "biases %s" % biases_update

			self.weights[i] = self.weights[i] - (eta/len(training_set))*weights_update
			self.biases[i] = self.biases[i] - (eta/len(training_set))*biases_update

	def sgd(self,training_set,eta,mini_batch_size=1):
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

	#	Useless for data from several files!
	def train(self,training_set,eta,epochs,method):
		if method == "bgd":
			for i in range(epochs):
				self.bgd(training_set,eta)
				print norm(self.apply(training_set[0][0])-np.array(training_set[0][1]))
				print "epoch: %s" % i
		elif method == "sgd":
			for i in range(epochs):
				self.sgd(training_set,eta)
				print norm(self.apply(training_set[0][0])-np.array(training_set[0][1]))
				print "epoch: %s" % i
		else:
			print "ERROR - Allowed methods: \"bgd\", \"sgd\""

	def randomize(self,training_set,epochs):
		for i in range(epochs):
			self.biases = [np.array([(random()-0.5)*0.001 for i in range(y)]) for y in self.sizes[1:]]
			self.weights = [(np.random.rand(y,x)-0.5)*0.001 for x,y in zip(self.sizes[:-1],self.sizes[1:])]
			print self.weights[0][0]
			print self.apply(training_set[0][0])
			print norm(self.apply(training_set[0][0])-np.array(training_set[0][1]))

class tanhNetwork(Network):

	def __init__(self,sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes

		self.biases = [np.array([(random()*2.0-1.0)/np.sqrt(y) for i in range(y)]) for y in sizes[1:]]
		self.weights = [np.random.randn(y,x)/np.sqrt(y) for x,y in zip(sizes[:-1],sizes[1:])]
		#self.biases = [np.random.randn(y,1) for y in sizes[1:]]	

	def apply(self,a_i,batch=False):

		if batch == False:

			a=np.array(a_i)

			for w,b in zip(self.weights,self.biases):
				a=tanh_vec(np.dot(w,a)+b)
				#a=tanh_vec(np.dot(w,a))

		elif batch == True:
			a=[np.array(a_k) for a_k in a_i]
			for i in range(len(a)):
				for w,b in zip(self.weights,self.biases):
					a[i]=tanh_vec(np.dot(w,a[i])+b)
					#a[i]=tanh_vec(np.dot(w,a[i]))
		return a

	def feed_forward(self,a_i):
		a_mat=[np.array(a_i)]

		for w,b in zip(self.weights,self.biases):
			a_mat.append(tanh_vec(np.dot(w,a_mat[-1])+b))
			#a_mat.append(tanh_vec(np.dot(w,a_mat[-1])))

		return a_mat

	def backprop(self,x,y):
		delta=[]

		a_mat = self.feed_forward(x)
		delta.append(a_mat[-1]-y)

		for w,a in zip(self.weights[-1:0:-1],a_mat[-2:0:-1]):
			delta.append(np.dot(w.transpose(),delta[-1])*(1-a*a))
			if max(delta[-1])>1.0 or min(delta[-1]) < 1.0:
				delta[-1] = delta[-1]/np.sqrt(sum([item**2 for item in delta[-1]]))
			#delta.append(np.dot(w.transpose(),delta[-1]))

		return delta[-1::-1], a_mat