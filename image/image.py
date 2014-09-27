
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
#from skimage import data
#from skimage.feature import blob_dog, blob_log, blob_doh
#from math import sqrt
from skimage.color import rgb2gray

from scipy.misc import imresize
import Image


img = Image.open("pics/captcha.jpg").convert("LA")

#img = mpimg.imread("pics/captcha.jpg")
#img = rgb2gray(img)

#img = imresize(img,0.1)

fig, ax = plt.subplots(1,1)

ax.imshow(img)
#ax.add_patch(plt.Circle((50, 50), 10, color="yellow", linewidth=2, fill=False))

plt.show()


