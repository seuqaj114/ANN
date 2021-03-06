from compr_set import get_training_set
from genetic.genetic import Body

import numpy as np
from random import random

training_set = get_training_set(8)

X_ = np.array([item[1] for item in training_set])
X_ = X_.transpose()

b2 = np.array([random() for i in range(103680)])
B2 = np.array([b2 for i in range(8)])
B2 = B2.transpose()

E = X_-B2

body = Body(E)
body.randomize(10000)

#A2 = np.dot(np.dot(X_-B2,(A1+B1).transpose()),linalg.inv(np.dot(A1+B1,(A1+B1).transpose())))