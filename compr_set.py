import numpy as np
import Image

def get_image_array(i):
	img = Image.open("pics/pic%s.jpg" % i).convert("LA")
	pic = [t[0]/255.0 for t in img.getdata()]

	return pic

def get_binary_array(i,size):
	binary_str = bin(i)[2:]
	binary = "0"*(int(np.log2(size))-len(binary_str)) + binary_str

	return map(int,[j for j in binary])

def get_training_set(size):
	training_set = [(get_binary_array(i,size),get_image_array(i)) for i in range(size)]

	return training_set