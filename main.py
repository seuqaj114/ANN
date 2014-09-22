import numpy as np
import sys
import time

import network
from generate import generate
from pprint import pprint
import misc

if __name__ == "__main__":
	newtork_geometry = [6,20,1]
	training_set = generate(30,6)
	net = network.Network(newtork_geometry)

	start = time.time()

	#	Training
	for i in range(0,100):
		net.sgd(training_set,2.0)

		output_set = net.apply([t[0] for t in training_set],True)
		desired_set = [t[1] for t in training_set]

		print "output=\n"
		print output_set
		print "desired=\n"
		print desired_set

		print "error=%s" % misc.set_norm(output_set,desired_set)


	finish = time.time()

	print "Time elapsed: %s\n" % (finish-start)
	pprint(net.apply([0.1,0.1,0.1,0.1,0.1,0.1]))