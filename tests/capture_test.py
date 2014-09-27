from image.capture import Stream, url

stream = Stream(url)

stream.collect(20,0.1)