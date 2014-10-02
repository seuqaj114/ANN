import sys
import network

from albert_fixtures import network_geometry, epochs, sample_size
from utils.session import load_session, save_session

import numpy as np

if __name__ == "__main__":
	net = network.Network(network_geometry)

	if len(sys.argv) > 1:
		if sys.argv[1] == "load":
			net.weights, net.biases = load_session()
			print "Parameters loaded"

	for i in range(epochs):
		for j in range(sample_size/10):
			training_input = np.load("data/pics%s.npy" % (j))
			training_output = np.load("data/output%s.npy" % (j))

			training_set = zip(training_input,training_output)

			net.bgd(training_set,2.0)

		print "epoch %s complete" % i

		print net.apply(np.load("data/pics4.npy")[-2])
		print net.apply(np.load("data/pics4.npy")[-1])


	save_session(net.weights,net.biases)