#importing modules
from PyQt4 import QtGui
from PyQt4 import QtCore

import sys
import time
import serial

class MainWindow(QtGui.QMainWindow):
  def __init__(self):
    QtGui.QMainWindow.__init__(self)
    self.setGeometry(50,50,300,200)
    self.serial = serial.Serial("/dev/ttyACM0",9600)

  def keyPressEvent(self,e):
    #print "Key pressed"
    if e.key() == 65:
      self.serial.write("a")
    elif e.key() == 87:
      self.serial.write("w")
    elif e.key() == 68:
      self.serial.write("d")
    elif e.key() == 83:
      self.serial.write("s")

  """
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
  """

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  window = MainWindow()
  window.show()

  app.exec_()