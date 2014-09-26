"""
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
#from skimage import data
#from skimage.feature import blob_dog, blob_log, blob_doh
#from math import sqrt
from skimage.color import rgb2gray

from scipy.misc import imresize

img = mpimg.imread("pic1.jpg")
#img_gray = rgb2gray(img)

img = imresize(img,0.1)

fig, ax = plt.subplots(1,1)

ax.imshow(img)
ax.add_patch(plt.Circle((50, 50), 10, color="yellow", linewidth=2, fill=False))

plt.show()
"""
import sys
from urllib import urlretrieve
from selenium import webdriver
import time

url = "http://192.168.1.5:8080"

driver = webdriver.Firefox()

driver.get(url)

driver.find_element_by_id("btn_play").click()

image = driver.find_element_by_id("live_image")
print image

start = time.time()

src = image.get_attribute("src")
print src

urlretrieve(src,"captcha.jpg")

finish = time.time()

print "Time elapsed: %s" % (finish-start)


