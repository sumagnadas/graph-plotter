#import the necessary modules
import sys
import random
import os.path as pt
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Qt, QPoint
import things as th


class NumInput(QtWidgets.QLineEdit):
    """Class which defines the input boxes for the coordinates"""
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(100)
        self.setMaxLength(4)
        onlyInt = QtGui.QIntValidator(-100, 100)
        self.setValidator(onlyInt)

class Graph(QtWidgets.QWidget):
    """Class which defines the window of the application"""
    def __init__(self, ctx, surface, line_color):
        super().__init__()

        self.image = QtWidgets.QLabel()# Image container for the graph
        text_margin = QtCore.QRect(0,0,10,10)

        #Input boxes for the first point of the line
        self.x_coord1 = NumInput()
        self.y_coord1 = NumInput()

        #Input boxes for the second point of the line
        self.x_coord2 = NumInput()# input boxes for the coordinates
        self.y_coord2 = NumInput()# input boxes for the coordinates

        #Buttons for plotting the graph and clearing the text boxes
        draw = QtWidgets.QPushButton(self.tr("Draw"))# 'Draw' Button to draw the line using coordinates of the point provided by the user
        clear = QtWidgets.QPushButton(self.tr("Reset"))# 'Reset' Button to clear everything in the input boxes

        #Widget containing the 'Draw' and 'Reset' button
        buttonBox = QtWidgets.QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(draw, QtWidgets.QDialogButtonBox.AcceptRole)
        buttonBox.addButton(clear, QtWidgets.QDialogButtonBox.RejectRole)

        #Connect the buttons to their respective functions so when one of the buttons is pressed, the respective function will be called
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        #Layout for the window
        self.layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom)
        self.layout.addWidget(self.image)
        self.makeGraphLayout("Point1",x=self.x_coord1,y=self.y_coord1)
        self.makeGraphLayout("Point2",x=self.x_coord2,y=self.y_coord2)
        self.layout.addWidget(buttonBox)
        self.setLayout(self.layout)

        #Some extra values for the implementation of the GUi
        self.ctx = ctx
        self.surface = surface
        self.line_color = line_color

    def setImage(self, filename):
        """Set the image for the graph"""
        self.graph_image = QtGui.QPixmap(pt.abspath(filename))
        self.image.setPixmap(self.graph_image)

    def accept(self):
        """Draw a line using the coordinates of the points provided by the user"""

        p1 = th.point(x=int(self.x_coord1.text()), y=int(self.y_coord1.text()))
        p2 = th.point(x=int(self.x_coord2.text()), y=int(self.y_coord2.text()))
        shape = th.Geometry()
        shape.draw_line(self.ctx, p1, p2, self.line_color, 0.005)
        filename = "/tmp/graph-{}.png".format(random.randint(1000,10000))
        self.surface.write_to_png(filename)
        self.graph_image = QtGui.QPixmap(pt.abspath(filename))
        self.image.setPixmap(self.graph_image)


    def reject(self):
        """Clear the text boxes if the user presses "Clear" button"""
        self.x_coord1.clear()
        self.y_coord1.clear()
        self.x_coord2.clear()
        self.y_coord2.clear()

    def makeGraphLayout(self,str,x,y):
        """Make the layout of the window"""
        self.layout.addWidget(QtWidgets.QLabel(str))
        self.layout.addWidget(QtWidgets.QLabel("X:"))
        self.layout.setDirection(QtWidgets.QBoxLayout.LeftToRight)
        self.layout.addWidget(x, Qt.AlignRight)
        self.layout.setDirection(QtWidgets.QBoxLayout.TopToBottom)
        self.layout.addWidget(QtWidgets.QLabel("Y:"))
        self.layout.setDirection(QtWidgets.QBoxLayout.LeftToRight)
        self.layout.addWidget(y, Qt.AlignRight)
