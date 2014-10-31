from numpy.linalg import norm
import numpy as np

#max of 2nd derivative of tanh: 0.761


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
