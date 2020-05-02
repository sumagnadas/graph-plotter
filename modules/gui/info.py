from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt


class ExtraInfo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QFormLayout()
        self.distance = QtWidgets.QLabel()
        self.totalSumAngle = QtWidgets.QLabel()
        self.sides = QtWidgets.QLabel()
        self.shapeType = QtWidgets.QLabel()

        layout.addRow('Length of the line:', self.distance)
        layout.addRow('Sum of all the angles:', self.totalSumAngle)
        layout.addRow('Number of sides:', self.sides)
        layout.addRow('Type of the shape\n(Regular or Irregular):', self.shapeType)

        self.setLayout(layout)
        self.hide()
