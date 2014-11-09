import numpy as np
from random import random
import sys
from math import sqrt

def euclid_distance(x,y):
	return sqrt(x**2+y**2)

def binarize_pixel(pixel):
	if pixel > 0.5:
		return 1
	else
		return 0

binarize_array = np.vectorize(binarize_pixel)

def kmeans(image,width,height):
	image = np.array(image)

	bin_image = binarize_array(image)

	if type(width) != int or type(height) != int:
		return "ERROR - width and height must be integers!"

	n_clusters = width*height

	clusters = [[random()*width,random()*height] for i in range(n_clusters)]

	#	proximity_array stores the points closer to each cluster center
	proximity_array
