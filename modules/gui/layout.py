from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
import os.path as pt

def makeGraphLayout(self,str,x,y):
    '''Make the layout of the window'''

    self.layout.addWidget(QtWidgets.QLabel(str))
    self.layout.addWidget(QtWidgets.QLabel("X:"))
    self.layout.setDirection(QtWidgets.QBoxLayout.LeftToRight)
    self.layout.addWidget(x, Qt.AlignRight)
    self.layout.setDirection(QtWidgets.QBoxLayout.TopToBottom)
    self.layout.addWidget(QtWidgets.QLabel("Y:"))
    self.layout.setDirection(QtWidgets.QBoxLayout.LeftToRight)
    self.layout.addWidget(y, Qt.AlignRight)

def makeWindowLayout(self, buttonBox):
    '''Make the layout of the window'''

    self.layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom)
    self.layout.addWidget(self.image)
    self.makeGraphLayout("Point1",x=self.x_coord1,y=self.y_coord1)
    self.makeGraphLayout("Point2",x=self.x_coord2,y=self.y_coord2)
    self.layout.addWidget(buttonBox)
    self.setLayout(self.layout)

def setImage(self, filename):
    '''Set the image for the graph'''

    self.graph_image = QtGui.QImage(pt.abspath(filename))
    self.image.setPixmap(QtGui.QPixmap().fromImage(self.graph_image))
