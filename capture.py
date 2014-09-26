import sys
from urllib import urlretrieve
import time

from selenium import webdriver

import Image
import numpy as np

url = "http://192.168.1.5:8080"

driver = webdriver.Firefox()

driver.get(url)

driver.find_element_by_id("btn_play").click()

image = driver.find_element_by_id("live_image")
print image

start = time.time()

src = image.get_attribute("src")
print src

urlretrieve(src,"pics/captcha.jpg")
img = Image.open("pics/captcha.jpg").convert("LA")
print img

pic = [t[0] for t in img.getdata()]

finish = time.time()

print "Time elapsed: %s" % (finish-start)

