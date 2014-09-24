from numpy.linalg import norm
import numpy as np

def average(vec):
	return sum(vec)/float(len(vec))

def set_norm(output_set,desired_set):
	norm_list = [norm(v1-v2) for v1,v2 in zip(output_set,desired_set)]

	return norm(norm_list)

# v1*v2T
def vvT(v1,v2):
	return v1.reshape((len(v1),1))*np.tile(v2,(len(v1),1))

def sigmoid(z):
	return 1.0/(1.0+np.exp(-z))

#	Loads weights and biases from data/*.npy
def load_session():
	weights = np.load("data/weights.npy")
	biases = np.load("data/biases.npy")

	return weights, biases

#	Saves weights and biases from data/*.npy
def save_session(weights,biases):
	np.save("data/weights.npy",weights)
	np.save("data/biases.npy",biases)

	print "Data saved."

	return 0
