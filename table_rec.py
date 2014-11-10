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

To do:
	- remove noise before cropping around table
"""

#	Only working for vertical tables by now!

ROWS = int(sys.argv[1])
COLS = int(sys.argv[2])
print "rows: %s; columns: %s" % (ROWS,COLS)

RATIO = min(float(ROWS)/COLS,float(COLS)/ROWS)

main_image = Image.open("pics/table.jpg").convert("LA")
print main_image.size

main_pic = [t[0] for t in main_image.getdata()]


MAX_GRAY = max(main_pic)
MIN_GRAY = min(main_pic)

print "max: %s; min %s" % (MAX_GRAY,MIN_GRAY)
print "average: %s" % ((MAX_GRAY+MIN_GRAY)/2)

contrast_image = main_image.point(lambda x: 0 if x <= (MAX_GRAY+MIN_GRAY)/2 else 255)
contrast_image = contrast_image.resize((contrast_image.size[0]/4,contrast_image.size[1]/4))
print contrast_image.size
contrast_image.show()


#	Look for a rectangle around the table in the image
rect_center = (contrast_image.size[0]/2,contrast_image.size[1]/2)
width = contrast_image.size[0]/2
height = contrast_image.size[1]/2

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

width_slope_array = [abs(width_count_array[i]-width_count_array[i-1]) for i in range(1,len(width_count_array))]
croped_width = width_slope_array.index(min(width_slope_array))

#pyplot.plot(width_count_array)
#pyplot.show()

height_count_array = []

inc=0
while rect_center[1]-(width/2+inc)> 0:
	croped_image = contrast_image.crop(map(int,(
		rect_center[0]-(width/2+croped_width)*RATIO,
		rect_center[1]-(height/2+inc),
		rect_center[0]+(width/2+croped_width)*RATIO,
		rect_center[1]+(height/2+inc)
		)))
	croped_pic = [t[0] for t in croped_image.getdata()]
	height_count_array.append(croped_pic.count(0))
	print height_count_array[-1]

	inc+=1

height_slope_array = [abs(height_count_array[i]-height_count_array[i-1]) for i in range(1,len(height_count_array))]
croped_height = height_slope_array.index(min(height_slope_array))



#pyplot.plot(height_slope_array)
#pyplot.show()

print "croped_width: %s" % croped_width
print "croped_height: %s" % croped_height

#	Display cropped image
croped_image = contrast_image.crop(map(int,(
		rect_center[0]-(width/2+croped_width)*RATIO,
		rect_center[1]-(height/2+croped_height),
		rect_center[0]+(width/2+croped_width)*RATIO,
		rect_center[1]+(height/2+croped_height)
		)))
#croped_image.show()

#	Draw the center of the estimated positions of the numbers
draw = ImageDraw.Draw(croped_image)
for i in range(ROWS):
	for j in range(COLS):
		draw.ellipse((
			(croped_image.size[0]/COLS)/2+j*(croped_image.size[0]/COLS)-4,
			(croped_image.size[1]/ROWS)/2+i*(croped_image.size[1]/ROWS)-4,
			(croped_image.size[0]/COLS)/2+j*(croped_image.size[0]/COLS)+4,
			(croped_image.size[1]/ROWS)/2+i*(croped_image.size[1]/ROWS)+4
		),fill=128)

croped_image.show()


"""
	Below, using height as reference!
"""

#	Run ever smaller rectangles over a cell to isolate the number
#	Just running over the top-left-most cell

#	The (0,0) cell
i = 0
j = 0

#	Set the search limits
WIDTH_MIN = j*croped_image.size[0]/COLS
WIDTH_MAX = croped_image.size[0]/COLS + j*croped_image.size[0]/COLS
HEIGHT_MIN = i*croped_image.size[1]/ROWS
HEIGHT_MAX = croped_image.size[1]/ROWS + i*croped_image.size[1]/ROWS

#	Set search rectangle's geometry
BASE_WIDTH = WIDTH_MAX - WIDTH_MIN
BASE_HEIGHT = HEIGHT_MAX - HEIGHT_MIN
RECT_CENTER = (WIDTH_MIN + BASE_WIDTH/2,HEIGHT_MIN+BASE_HEIGHT/2)

#	Set rectangle's ratio ( > 0 )
RECT_RATIO = float(BASE_WIDTH)/BASE_HEIGHT

#	Search cicle, rectangles from outside to center
cell_count_array = []
for inc in range(BASE_HEIGHT/2):
	croped_cell = croped_image.crop(map(int,(
		RECT_CENTER[0]-(BASE_WIDTH/2-inc*RECT_RATIO),
		RECT_CENTER[1]-(BASE_HEIGHT/2-inc),
		RECT_CENTER[0]+(BASE_WIDTH/2-inc*RECT_RATIO),
		RECT_CENTER[1]+(BASE_HEIGHT/2-inc)
		)))

	croped_cell_pic = [t[0] for t in croped_cell.getdata()]
	cell_count_array.append(croped_cell_pic.count(0))
	print cell_count_array[-1]

#	Find minimum of number of pixels rate of change
cell_slope_array = [abs(cell_count_array[i]-cell_count_array[i-1]) for i in range(1,len(cell_count_array))]
cell_height = cell_slope_array.index(min(cell_slope_array))

pyplot.plot(cell_slope_array)
pyplot.show()

#	Get croped cell (final)
croped_cell = croped_image.crop(map(int,(
		RECT_CENTER[0]-(BASE_WIDTH/2-cell_height*RECT_RATIO),
		RECT_CENTER[1]-(BASE_HEIGHT/2-cell_height),
		RECT_CENTER[0]+(BASE_WIDTH/2-cell_height*RECT_RATIO),
		RECT_CENTER[1]+(BASE_HEIGHT/2-cell_height)
		)))

croped_cell.show()