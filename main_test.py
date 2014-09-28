import numpy as np
import sys
import time

import network
from generate import generate
import sys

from pprint import pprint
from utils.math import set_norm

if __name__ == "__main__":

	newtork_geometry = [2,2,1]
	#training_set = generate(100,6)
	training_set = [([1,0],[1]),([1,1],[0]),([0,1],[1]),([0,0],[0])]
	net = network.Network(newtork_geometry)

	start = time.time()

	#	Training
	for i in range(0,100):
		net.bgd(training_set,1.0)

		output_set = net.apply([t[0] for t in training_set],True)
		desired_set = [t[1] for t in training_set]
		error = set_norm(output_set,desired_set)
		
		"""
		print "\n"
		print "output="
		print output_set
		print "desired="
		print desired_set
		print "error=%s" % error
		"""

		"""
		if error < 0.00001:
			print "epochs: %s" % (i)
			break
		"""
		print "epoch: %s" % i

	finish = time.time()

	print "Time elapsed: %s\n" % (finish-start)

	"""
	print net.weights
	print net.biases
	print "Applying"
	print net.apply([1,0])
	print net.apply([1,1])
	print net.apply([0,1])
	print net.apply([0,0])
	"""
	#pprint(net.apply([0.1,0.1,0.1,0.1,0.1,0.1]))
