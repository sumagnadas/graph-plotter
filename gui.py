import sys, random
import os.path as pt
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Qt, QPoint
import things as th

class NumInput(QtWidgets.QLineEdit):
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(100)
        self.setMaxLength(4)
        onlyInt = QtGui.QIntValidator(-100, 100)
        self.setValidator(onlyInt)

class Graph(QtWidgets.QWidget):
    def __init__(self, ctx, surface, line_color):
        super().__init__()
        self.image = QtWidgets.QLabel()
        text_margin = QtCore.QRect(0,0,10,10)
        self.x_coord1 = NumInput()
        self.y_coord1 = NumInput()
        self.x_coord2 = NumInput()
        self.y_coord2 = NumInput()
        draw = QtWidgets.QPushButton(self.tr("Draw"))
        clear = QtWidgets.QPushButton(self.tr("Reset"))
        buttonBox = QtWidgets.QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(draw, QtWidgets.QDialogButtonBox.AcceptRole)
        buttonBox.addButton(clear, QtWidgets.QDialogButtonBox.RejectRole)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom)
        self.layout.addWidget(self.image)
        self.makeGraphLayout("Point1",x=self.x_coord1,y=self.y_coord1)
        self.makeGraphLayout("Point2",x=self.x_coord2,y=self.y_coord2)
        self.layout.addWidget(buttonBox)

        self.setLayout(self.layout)
        self.ctx = ctx
        self.surface = surface
        self.line_color = line_color

    def setImage(self, filename):
        self.graph_image = QtGui.QPixmap(pt.abspath(filename))
        self.image.setPixmap(self.graph_image)

    def accept(self):
        p1 = th.point(x=int(self.x_coord1.text()), y=int(self.y_coord1.text()))
        p2 = th.point(x=int(self.x_coord2.text()), y=int(self.y_coord2.text()))
        shape = th.Geometry()
        shape.draw_line(self.ctx, p1, p2, self.line_color)
        self.surface.write_to_png("graph.png")
        self.graph_image = QtGui.QPixmap(pt.abspath("graph.png"))
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

    def getCoord(self):
        return int(self.x_coord.text()), int(self.y_coord.text())
