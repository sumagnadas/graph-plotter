from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
import os.path as pt


def makeGraphLayout(self, str, x, y):
    '''Make the layout of the window'''
    inputLayout = QtWidgets.QFormLayout()
    inputLayout.addRow(QtWidgets.QLabel(str))
    inputLayout.addRow(QtWidgets.QLabel("X:"), x)
    inputLayout.addRow(QtWidgets.QLabel("Y:"), y)
    self.windowLayout.addLayout(inputLayout)


def makeWindowLayout(self, buttonBox):
    '''Make the layout of the window'''

    self.windowLayout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
    self.windowLayout.addWidget(self.image)
    self.makeGraphLayout("Point1", x=self.x_coord1, y=self.y_coord1)
    self.makeGraphLayout("Point2", x=self.x_coord2, y=self.y_coord2)
    self.windowLayout.addWidget(buttonBox)
    self.setLayout(self.windowLayout)


def setImage(self, filename):
    '''Set the image for the graph'''

    self.graph_image = QtGui.QImage(pt.abspath(filename))
    self.image.setPixmap(QtGui.QPixmap().fromImage(self.graph_image))
