#importing modules
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import time
from urllib import urlretrieve

from selenium import webdriver

from utils import misc
from albert_fixtures import sample_size, url

import Image
import numpy as np
import serial

class MainWindow(QtGui.QMainWindow):
  def __init__(self,url,sample_size):
    QtGui.QMainWindow.__init__(self)
    self.setGeometry(200,200,600,400)
    self.serial = serial.Serial("/dev/ttyACM0",9600)

    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.timerTick)

    self.a = [0]*4
    self.driver = webdriver.Firefox()
    self.driver.get(url)

    self.driver.find_element_by_id("btn_play").click()

    self.image = self.driver.find_element_by_id("live_image")

    self.frame_list = []
    self.output_list = []
    self.i = 0
    self.sample_size = sample_size

  def keyPressEvent(self,e):
    #print "Key pressed"
    if e.key() == 65:
      self.a[0]=1
    if e.key() == 87:
      self.a[1]=1
    if e.key() == 68:
      self.a[2]=1
    if e.key() == 83:
      self.a[3]=1

  def keyReleaseEvent(self,e):
    #print "Key released"
    if e.key() == 65:
      self.a[0]=0
    if e.key() == 87:
      self.a[1]=0
    if e.key() == 68:
      self.a[2]=0
    if e.key() == 83:
      self.a[3]=0

  def timerTick(self):
    print self.a

    src = self.image.get_attribute("src")
    print src

    urlretrieve(src,"pics/captcha.jpg")
    print "Image %s captured." % self.i
    img = Image.open("pics/captcha.jpg").convert("LA")
    pic = [t[0]/255.0 for t in img.getdata()]

    if (self.i+1)/10 != self.i/10:
      np.save("data/pics%s.npy" % (self.i/10),self.frame_list)
      np.save("data/output%s.npy" % (self.i/10),self.output_list)
      print "Output %s" % self.output_list
      print "File %s saved" % (self.i/10)
      self.frame_list = []
      self.output_list = []
    else:
      self.frame_list.append(pic)
      self.output_list.append(list(self.a))
      print self.output_list

      
      if self.a[1] == 1 and self.a[0] == 0 and self.a[2] == 0:
        self.serial.write("w") 
      elif self.a[1] == 1 and self.a[0] == 1 and self.a[2] == 0:
        self.serial.write("r") #wa
      elif self.a[1] == 1 and self.a[0] == 0 and self.a[2] == 1:
        self.serial.write("t") #wd
      elif self.a[3] == 1 and self.a[0] == 0 and self.a[2] == 0:
        self.serial.write("s") 
      elif self.a[3] == 1 and self.a[0] == 1 and self.a[2] == 0:
        self.serial.write("y") #sa
      elif self.a[3] == 1 and self.a[0] == 0 and self.a[2] == 1:
        self.serial.write("u")  #sd
      
    self.i += 1
    if self.i >= self.sample_size:
      self.timer.stop()
      print "Done!"

time_step = 1000 #miliseconds

app = QtGui.QApplication(sys.argv)
window = MainWindow(url,sample_size)
window.show()

misc.countdown(3)

window.timer.start(time_step)

app.exec_()