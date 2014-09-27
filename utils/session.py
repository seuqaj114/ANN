import numpy as np

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