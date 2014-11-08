import numpy as np
import Image

def get_image_array(i,normalized=True):
	img = Image.open("pics/pic%s.jpg" % i).convert("LA")

	if normalized == True:
		pic = [((t[0]/255.0)*2.0-1.0)*0.761 for t in img.getdata()]
	else:
		pic = [t[0] for t in img.getdata()]

	return pic

def get_binary_array(i,size):
	binary_str = bin(i)[2:]
	binary = "0"*(int(np.log2(size))-len(binary_str)) + binary_str

	return map(int,[j for j in binary])

def get_normalized_binary_array(i,size):
	binary_str = bin(i)[2:]
	binary = "0"*(int(np.log2(size))-len(binary_str)) + binary_str
	binary_array = np.array(map(float,[j for j in binary]))

	binary_array = binary_array - sum(binary_array)/len(binary_array)

	return list(binary_array)

def get_binary_extended_array(i,size):
	binary = [0]*size
	binary[i] = 1
	return binary

def get_training_set(size):
	training_set = [(get_normalized_binary_array(i,size),get_image_array(i)) for i in range(size)]

	return training_set