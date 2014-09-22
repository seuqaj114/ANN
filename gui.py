import numpy as np
import sys
import time

from PyQt4 import QtGui
from PyQt4 import QtCore

import network

"""
Training the OR function
"""

def train():
	global net
	global window

	for i in range(0,100):
		time.sleep(0.1)
		net.gd(training_set,5.0)
		window.update(net.feed_forward([1,0]))

class MainWindow(QtGui.QWidget):
	def __init__(self,newtork_geometry):
		QtGui.QWidget.__init__(self)

		self.h_ref = 100
		self.v_ref = 100
		self.h_step = 50
		self.v_step = 30

		self.setGeometry(200,200,600,400)
		self.setWindowTitle("Neural network")

		self.qbtn=QtGui.QPushButton(self)
		self.qbtn.setText("Start")
		self.qbtn.setObjectName("start")
		self.qbtn.clicked.connect(train)
		self.qbtn.setFixedSize(50,50)
		self.qbtn.move(50,50)

		self.btns=[]
		for l in range(len(newtork_geometry)):
			self.btns.append([])
			for i in range(newtork_geometry[l]):
				btn=QtGui.QPushButton(self)
				btn.setFixedSize(20,20)
				btn.move(self.h_ref+l*self.h_step,self.v_ref+i*self.v_step)
				btn.setStyleSheet("background-color: rgba(%s,%s,%s,255)" % (100,100,100))
				self.btns[l].append(btn)

	def update(self,a_mat):
		for i in range(len(a_mat)):
			for j in range(len(a_mat[i])):
				color = int(255.0*a_mat[i][j])
				self.btns[i][j].setStyleSheet("background-color: rgba(%s,%s,%s,255)" % (color,color,color))

if __name__ == "__main__":
	newtork_geometry = [2,2,1]
	training_set = [([1,0],[1]),([0,1],[1]),([0,0],[0]),([1,1],[1])]
	net = network.Network(newtork_geometry)

	app = QtGui.QApplication(sys.argv)
	window = MainWindow(newtork_geometry)
	window.show()

	sys.exit(app.exec_())