import numpy as np
import sys
import time

import network
from generate import generate
from pprint import pprint

if __name__ == "__main__":
	newtork_geometry = [6,30,1]
	training_set = generate(1000,6)
	net = network.Network(newtork_geometry)

	"""
	Training
	"""
	for i in range(0,200):
		net.bgd(training_set,2.0)

	print "\n"
	pprint(net.apply([0.1,0.1,0.1,0.1,0.1,0.1]))