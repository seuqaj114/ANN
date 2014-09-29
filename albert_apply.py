import sys
import network
import time
from urllib import urlretrieve

from albert_fixtures import network_geometry, epochs, sample_size, url
from utils.session import load_session, save_session

from selenium import webdriver

import Image
import numpy as np

if __name__ == "__main__":
	net = network.Network(network_geometry)
	
	net.weights, net.biases = load_session()
	print "Parameters loaded"

	driver = webdriver.Firefox()
	driver.get(url)

	driver.find_element_by_id("btn_play").click()

	image = driver.find_element_by_id("live_image")

	for i in range(100):
		src = image.get_attribute("src")
		urlretrieve(src,"pics/captcha.jpg")
		print "Image captured."
		img = Image.open("pics/captcha.jpg").convert("LA")
		pic = [t[0]/255.0 for t in img.getdata()]

		if net.apply(pic)[0] > 0.9:
			print "Sim"
		else:
			print "Nao" 

		time.sleep(1)

	#l = np.load("data/pics3.npy")
	#o = np.load("data/output3.npy")

	#print o[8]
	#print net.apply(l[8])

