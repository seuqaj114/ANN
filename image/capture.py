import sys
import time
from urllib import urlretrieve

from selenium import webdriver

import Image
import numpy as np

from utils import misc

url = "http://192.168.1.2:8080"

class Stream():
	#	Opens selenium firefox instance, sets resolution (TO DO) and returns driver and image element
	def __init__(self,url):
		self.driver = webdriver.Firefox()
		self.driver.get(url)

		self.driver.find_element_by_id("btn_play").click()

		self.image = self.driver.find_element_by_id("live_image")

	def collect(self,sample_size,time_gap):
		frame_list = []
		output_list = []

		misc.countdown(3)

		for i in range(sample_size):
			src = self.image.get_attribute("src")
			print src

			urlretrieve(src,"pics/captcha.jpg")
			print "Image %s captured." % i
			img = Image.open("pics/captcha.jpg").convert("LA")
			pic = [t[0] for t in img.getdata()]

			if (i+1)/10 != i/10:
				np.save("data/pics%s.npy" % (i/10),frame_list)
				print "File %s saved" % (i/10)
			else:
				frame_list.append(pic)

			time.sleep(time_gap)


		#np.save("data/pics.npy",frame_list)
		print "Data capture done!"



