from urllib import urlretrieve
from selenium import webdriver
import time
import sys

from albert_fixtures import url

from PySide import QtGui
from PySide import QtCore
from PySide.QtWebKit import QWebView, QWebSettings

app = QtGui.QApplication(sys.argv)

win = QWebView()

win.setUrl(QtCore.QUrl(url))

print "Getting frame..."
frame = win.page().mainFrame().documentElement()
print dir(win.page())

print "Getting button..."
button = frame.findFirst("#video_mode > label:nth-child(5)")
button.evaluateJavaScript("this.click()")

print "Getting image..."
image = frame.findFirst("#img1")

print "Done."
win.show()
app.exec_()

'''

print "Opening..."

driver = webdriver.Firefox()
driver.get("http://192.168.1.9:8080/")
driver.find_element_by_xpath('//*[@id="video_mode"]/label[5]').click()

time.sleep(2)

print "Looking for image..."
image = driver.find_element_by_id('img1')

time.sleep(2)

print "Capturing src..."
src = image.get_attribute("src")

print "Saving image..."
urlretrieve(src,"pics/pic234.jpg")

print "Process complete."

'''

