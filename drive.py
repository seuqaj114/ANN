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
  def __init__(self):
    QtGui.QMainWindow.__init__(self)
    self.setGeometry(200,200,600,400)
    self.serial = serial.Serial("/dev/ttyACM0",9600)

    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.timerTick)

    self.a = [0]*4

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

    if self.a[1] == 1 and self.a[0] == 0 and self.a[2] == 0:
      self.serial.write("w") 
    elif self.a[1] == 1 and self.a[0] == 1 and self.a[2] == 0:
      self.serial.write("wa")
    elif self.a[1] == 1 and self.a[0] == 0 and self.a[2] == 1:
      self.serial.write("wd")
    if self.a[3] == 1 and self.a[0] == 0 and self.a[2] == 0:
      self.serial.write("s") 
    elif self.a[3] == 1 and self.a[0] == 1 and self.a[2] == 0:
      self.serial.write("sa")
    elif self.a[3] == 1 and self.a[0] == 0 and self.a[2] == 1:
      self.serial.write("sd")  

    """
    if self.a[0] == 1:
      self.serial.write("a")
     
    if self.a[2] == 1:
      self.serial.write("d")  
    if self.a[3] == 1:
      self.serial.write("s")
    """

time_step = 1000 #miliseconds

app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()

misc.countdown(3)

window.timer.start(time_step)

app.exec_()