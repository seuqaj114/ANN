import numpy as np 
import Image, ImageDraw
import sys
import matplotlib.pyplot as pyplot

"""
Steps: 
	- expand values to full range
	- crop around table
	- increase contrast
	- further contrast (to binary)
	- downsample
	- find clusters

"""

#	Only working for vertical tables by now!

ROWS = int(sys.argv[1])
COLS = int(sys.argv[2])
print "rows: %s; columns: %s" % (ROWS,COLS)

RATIO = min(float(ROWS)/COLS,float(COLS)/ROWS)

main_image = Image.open("pics/table.jpg").convert("LA")

main_pic = [t[0] for t in main_image.getdata()]

MAX_GRAY = max(main_pic)
MIN_GRAY = min(main_pic)

print "max: %s; min %s" % (MAX_GRAY,MIN_GRAY)
print "average: %s" % ((MAX_GRAY+MIN_GRAY)/2)

contrast_image = main_image.point(lambda x: 0 if x <= (MAX_GRAY+MIN_GRAY)/2 else 255)
#contrast_image.show()

print main_image.size


#	Look for a rectangle around the table in the image

rect_center = (main_image.size[0]/2,main_image.size[1]/2)
width = main_image.size[0]/2
height = main_image.size[1]/2

width_count_array = []

#for inc in range(600):
inc=0
while rect_center[0]-(width/2+inc)*RATIO > 0:
	croped_image = contrast_image.crop(map(int,(
		rect_center[0]-(width/2+inc)*RATIO,
		rect_center[1]-(height/2),
		rect_center[0]+(width/2+inc)*RATIO,
		rect_center[1]+(height/2)
		)))
	croped_pic = [t[0] for t in croped_image.getdata()]
	width_count_array.append(croped_pic.count(0))
	print width_count_array[-1]

	inc+=1

width_slope_array = [width_count_array[i]-width_count_array[i-1] for i in range(1,len(width_count_array))]
croped_width = width_slope_array.index(min(width_slope_array))

#pyplot.plot(count_array)
#pyplot.show()

height_count_array = []

inc=0
while rect_center[1]-(width/2+inc)> 0:
	croped_image = contrast_image.crop(map(int,(
		rect_center[0]-(width/2)*RATIO,
		rect_center[1]-(height/2+inc),
		rect_center[0]+(width/2)*RATIO,
		rect_center[1]+(height/2+inc)
		)))
	croped_pic = [t[0] for t in croped_image.getdata()]
	height_count_array.append(croped_pic.count(0))
	print height_count_array[-1]

	inc+=1

height_slope_array = [height_count_array[i]-height_count_array[i-1] for i in range(1,len(height_count_array))]
croped_height = height_slope_array.index(min(height_slope_array))

pyplot.plot(height_count_array)
pyplot.show()

#	Display cropped image

croped_image = contrast_image.crop(map(int,(
		rect_center[0]-(width/2+croped_width)*RATIO,
		rect_center[1]-(height/2+croped_height),
		rect_center[0]+(width/2+croped_width)*RATIO,
		rect_center[1]+(height/2+croped_height)
		)))
croped_image.show()



"""
draw = ImageDraw.Draw(contrast_image)
draw.rectangle((rect_center[0]-width/2*RATIO,rect_center[1]-height/2,rect_center[0]+width/2*RATIO,rect_center[1]+height/2),outline=128)
"""

#contrast_image.show()




