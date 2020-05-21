from PySide2.QtCore import Qt
from PySide2 import QtGui, QtWidgets

filename = ''


class NumInput(QtWidgets.QLineEdit):
    """Class which defines the input boxes for the coordinates"""
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(100)
        self.setMaxLength(4)
        onlyInt = QtGui.QIntValidator(-20, 20)
        self.setValidator(onlyInt)
        self.setText("0")
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum,
                           QtWidgets.QSizePolicy.Minimum)

    def setzero(self):
        if self.text() == '':
            self.setText('0')

class PointInput(QtWidgets.QWidget):
    def __init__(self, str, x, y):
        super().__init__()
        self.removeButton = QtWidgets.QPushButton('')
        self.removeButton.setStyleSheet('border: transparent')
        self.removeButton.hide()
        self.layout = QtWidgets.QFormLayout()
        str = QtWidgets.QLabel(str)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(str)
        layout.addSpacing(0)
        layout.addWidget(self.removeButton)
        self.layout.addRow(layout)
        self.layout.addRow('X:', x)
        self.layout.addRow('Y:', y)
        self.setLayout(self.layout)
        self.x = x
        self.y = y

    def addRow(self, layout):
        self.layout.addRow(layout)

    def insertRow(self, layout):
        self.layout.insertRow(0, layout)

    def xy(self):
        return [self.x, self.y]
