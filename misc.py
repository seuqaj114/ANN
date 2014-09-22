from numpy.linalg import norm

def average(vec):
	return sum(vec)/float(len(vec))

def set_norm(output_set,desired_set):
	norm_list = [norm(v1-v2) for v1,v2 in zip(output_set,desired_set)]

	return norm(norm_list)