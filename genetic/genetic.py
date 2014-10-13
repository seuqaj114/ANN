import random

import numpy as np
from numpy.linalg import norm

class Body():
	#	This class solves the problem of finding two matrices to solve the problem
	#	A1*A2 = E
	def __init__(self,desired,size1=(103680,3),size2=(3,8)):

		if type(desired).__name__ == "ndarray":
			self.E = desired
		else:
			self.E = np.array(desired)

		self.A1 = np.random.rand(*size1)
		self.A2 = np.random.rand(*size2)

		self.diff = norm(np.dot(A1,A2)-self.E)

