import sys
import os
import time

from urllib import urlretrieve

from selenium import webdriver
from utils import misc
from albert_fixtures import sample_size, url

import Image
import numpy as np



if __name__=="__main__":

	driver = webdriver.Firefox()
	driver.get(url)
	driver.find_element_by_id("btn_play").click()

	image = driver.find_element_by_id("live_image")

	for i in range(8):
		src = image.get_attribute("src")
		print src

		urlretrieve(src,"pics/pic%s.jpg" % i)
		print "Image %s captured." % i
		time.sleep(1)
