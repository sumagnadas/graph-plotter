#import the necessary modules
import sys
import random
import os.path as pt
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import *

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
    def __init__(self, ctx, surface, line_color, backup):
        super().__init__()

        self.draw = False
        self.save = False
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
        clear = QtWidgets.QPushButton(self.tr("Clear"))# 'Reset' Button to clear everything in the input boxes
        save = QtWidgets.QPushButton(self.tr("Save this Graph"))

        #Widget containing the 'Draw', 'Save this Graph' and 'Reset' button
        buttonBox = QtWidgets.QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(draw, QtWidgets.QDialogButtonBox.AcceptRole)
        buttonBox.addButton(clear, QtWidgets.QDialogButtonBox.RejectRole)

        #Connect the buttons to their respective functions so when one of the buttons is pressed, the respective function will be called
        buttonBox.accepted.connect(self.draw)
        buttonBox.rejected.connect(self.clear)

        #Layout for the window
        self.layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom)
        self.layout.addWidget(self.image)
        self.makeGraphLayout("Point1",x=self.x_coord1,y=self.y_coord1)
        self.makeGraphLayout("Point2",x=self.x_coord2,y=self.y_coord2)
        self.layout.addWidget(buttonBox)
        self.setLayout(self.layout)

        # Some extra values for the implementation of the GUi
        self.ctx = ctx
        self.back_ctx = backup[0]
        self.back_surface = backup[1]
        self.surface = surface
        self.line_color = line_color

    def setImage(self, filename):
        """Set the image for the graph"""
        self.graph_image = QtGui.QImage(pt.abspath(filename))
        self.image.setPixmap(QtGui.QPixmap().fromImage(self.graph_image))

    def draw(self):
        """Draw a line using the coordinates of the points provided by the user"""

        self.image.update()
        self.p1 = geometry.point(x=int(self.x_coord1.text()), y=int(self.y_coord1.text()))
        self.p2 = geometry.point(x=int(self.x_coord2.text()), y=int(self.y_coord2.text()))
        shape = geometry.Geometry()

        shape.draw_line(self.ctx, self.p1, self.p2, self.line_color, 0.005)
        filename = "/tmp/graph-{}.png".format(random.randint(1000,10000))
        self.surface.write_to_png(filename)
        self.graph_image = QtGui.QImage()
        self.graph_image.load(pt.abspath(filename))
        self.image.setPixmap(QtGui.QPixmap().fromImage(self.graph_image))
        self.draw = True
        self.image.repaint()


    def clear(self):
        """Clear the text boxes if the user presses "Clear" button and also the grid"""

        self.x_coord1.clear()
        self.y_coord1.clear()
        self.x_coord2.clear()
        self.y_coord2.clear()
        self.image.setPixmap("graph.png")
        self.ctx.set_source_surface(self.back_surface)
        #self.ctx.paint()

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

    def paintEvent(self, e):
        if self.draw:
            p = QtGui.QPainter()
            p.begin(self)
            p.drawLine(self.p1.x*200,self.p1.y*200,self.p2.x*200,self.p2.y*200)
            p.end()
            self.draw = False

    def show(self):
        super().show()
