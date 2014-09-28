#importing modules
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import time

from selenium import webdriver

from utils import misc

class MainWindow(QtGui.QMainWindow):
  def __init__(self,url):
    QtGui.QMainWindow.__init__(self)
    self.setGeometry(200,200,600,400)

    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.timerTick)

    self.a = [0]*4
    self.driver = webdriver.Firefox()
    self.driver.get(url)

    self.driver.find_element_by_id("btn_play").click()

    self.image = self.driver.find_element_by_id("live_image")

    self.frame_list = []
    self.output_list = []

  def keyPressEvent(self,e):
    #print "Key pressed"
    if e.key() == 65:
      self.a[0]=1
    elif e.key() == 87:
      self.a[1]=1
    elif e.key() == 68:
      self.a[2]=1
    elif e.key() == 83:
      self.a[3]=1

  def keyReleaseEvent(self,e):
    #print "Key released"
    if e.key() == 65:
      self.a[0]=0
    elif e.key() == 87:
      self.a[1]=0
    elif e.key() == 68:
      self.a[2]=0
    elif e.key() == 83:
      self.a[3]=0

  def timerTick(self):
    print self.a

url = "http://192.168.1.2:8080"

app = QtGui.QApplication(sys.argv)
window = MainWindow(url)
window.show()

misc.countdown(3)

window.timer.start(1000)

app.exec_()
