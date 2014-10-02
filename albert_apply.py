import sys
import network
import time
from urllib import urlretrieve

from albert_fixtures import network_geometry, epochs, sample_size, url
from utils.session import load_session, save_session

from selenium import webdriver

import Image
import numpy as np
import serial

if __name__ == "__main__":
	net = network.Network(network_geometry)
	
	net.weights, net.biases = load_session()
	print "Parameters loaded"

	serial = serial.Serial("/dev/ttyACM0",9600)

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

		a = net.apply(pic)
		print a

		if a[1] > 0.5 and a[0] <= 0.5 and a[2] <= 0.5:
		  serial.write("w") 
		elif a[1] > 0.5 and a[0] > 0.5 and a[2] <= 0.5:
		  serial.write("r") #wa
		elif a[1] > 0.5 and a[0] < 0.5 and a[2] > 0.5:
		  serial.write("t") #wd
		elif a[3] > 0.5 and a[0] <= 0.5 and a[2] <= 0.5:
		  serial.write("s") 
		elif a[3] > 0.5 and a[0] > 0.5 and a[2] <= 0.5:
		  serial.write("y") #sa
		elif a[3] > 0.5 and a[0] <= 0.5 and a[2] > 0.5:
		  serial.write("u")  #sd


		time.sleep(1)

	#l = np.load("data/pics3.npy")
	#o = np.load("data/output3.npy")

	#print o[8]
	#print net.apply(l[8])

