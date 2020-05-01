from PySide2.QtCore import Qt
from PySide2 import QtGui, QtWidgets

filename = ''


class NumInput(QtWidgets.QLineEdit):
    """Class which defines the input boxes for the coordinates"""
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(100)
        self.setMaxLength(4)
        onlyInt = QtGui.QIntValidator(-300, 300)
        self.setValidator(onlyInt)
        self.setText("0")
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

    def setzero(self):
        if self.text() == '':
            self.setText('0')

class ShapeList(QtWidgets.QComboBox):

    def __init__(self):
        super().__init__()
        self.addItems(['Line', 'Triangle', 'Quadrilateral', 'Polygon'])
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

class PointInput(QtWidgets.QWidget):
    def __init__(self, str, x, y):
        super().__init__()
        self.layout = QtWidgets.QFormLayout()
        self.layout.addRow(QtWidgets.QLabel(str))
        self.layout.addRow('X:', x)
        self.layout.addRow('Y:', y)
        self.setLayout(self.layout)

    def addRow(self, layout):
        self.layout.addRow(layout)

    def insertRow(self, layout):
        self.layout.insertRow(0, layout)
