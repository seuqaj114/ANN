import numpy as np
from random import random
import sys
from math import sqrt

def euclid_distance(x1,x2):
	#	x1 and x2 must be array-like objects
	return sqrt((x1[0]-x2[0])**2+(x1[1]-x2[1])**2)

def kmeans(image,width,height,epochs,clusters=None):

	if type(width) != int or type(height) != int:
		return "ERROR - width and height must be integers!"

	image = np.array(image)

	dots = []
	for i in range(len(image)):
		for j in range(len(image[i])):
			if image[i][j] < 140:
				dots.append([i,j])

	print "Dots: %s" % (len(dots))

	n_clusters = width*height

	if not clusters:
		clusters = [[random()*width,random()*height] for i in range(n_clusters)]

	for j in range(epochs):
		print j
		location_array = np.array([[0,0]]*n_clusters)
		count_array = [0]*n_clusters

		for dot in dots:
			distance_array = [euclid_distance(dot,cluster) for cluster in clusters]
			min_index = distance_array.index(min(distance_array))
			location_array[min_index] += np.array(dot)
			count_array[min_index] += 1
			#print count_array

		clusters = [location/count for location, count in zip(location_array,count_array)]

	return clusters

