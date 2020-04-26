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

    def setzero(self):
        if self.text() == '':
            self.setText('0')
