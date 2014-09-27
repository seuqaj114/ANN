import time

def countdown(seconds):
	print "Starting in %s" % seconds

	for i in range(seconds)[::-1]:
		time.sleep(1)
		print i
