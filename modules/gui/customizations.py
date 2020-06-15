from PySide2.QtCore import Qt
from PySide2 import QtGui, QtWidgets
from modules import configureImage, draw_grid
from os.path import isfile


class CustomizeMenu(QtWidgets.QMenu):
    def __init__(self, title, widget, width, height, parent=None):
        super().__init__(title, parent)
        self.addAction("Change the colours of the graph", lambda: self.changeColour(window, widget))
        theme = self.addMenu("Change the theme of the window")
        theme.addAction("Light(Default)", lambda: self.setLight(widget))
        theme.addAction("Dark", lambda: self.setDark(widget))
        window =  CustomizeDialog(widget)

    def scale(self, widget, width, height, square=20):
        print(20)

    def changeColour(self, changer, widget):
        changer.exec_()
        def changeGridColour(widget):
            self.gridcolor = QtWidgets.QColorDialog.getColor(initial=Qt.black, title="Select colour for the grid.")
            bg = configureImage(widget.graph_image.width(), widget.graph_image.height(), self.gridcolor, self.bgcolor)
            widget.graph_image = bg
            widget.image.setPixmap(QtGui.QPixmap().fromImage(widget.graph_image))

        def changeBGColour(widget):
            self.bgcolor = QtWidgets.QColorDialog.getColor(title="Select colour for the background of the graph")
            bg = configureImage(widget.graph_image.width(), widget.graph_image.height(), self.gridcolor, self.bgcolor)
            widget.graph_image = bg
            widget.image.setPixmap(QtGui.QPixmap().fromImage(widget.graph_image))

        def changeLineColour(widget):
            pencolor = QtWidgets.QColorDialog.getColor(initial=Qt.black, title="Select colour for the lines to be drawn")
            widget.pencolor = pencolor

    def setLight(self, widget):
        widget.setStyleSheet('background: #efefef ')
        widget.setStyleSheet('QMenu::item:selected{background: transparent; color: #000099}')

    def setDark(self, widget):
        widget.setStyleSheet("background: grey")

class CustomizeDialog(QtWidgets.QDialog):
    def __init__(self, widget):
        super().__init__(widget)

        layout = QtWidgets.QVBoxLayout()
        button1 = QtWidgets.QPushButton("Change the colour of the grid", clicked=lambda: self.changeGridColour(widget))
        button2 = QtWidgets.QPushButton("Change the background colour of the graph", clicked=lambda: self.changeBGColour(widget))
        button3 = QtWidgets.QPushButton("Change the colour of the lines to be\n drawn on the graph", clicked=lambda: self.changeLineColour(widget))
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        self.setLayout(layout)

        self.bgcolor = QtGui.QColor(0, 0, 0, 0)
        self.gridcolor = QtGui.QColor(0, 0, 0)

    def changeGridColour(self, widget):
        self.gridcolor = QtWidgets.QColorDialog.getColor(initial=Qt.black, title="Select colour for the grid.")
        bg = configureImage(widget.graph_image.width(), widget.graph_image.height(), self.gridcolor, self.bgcolor)
        widget.graph_image = bg
        widget.image.setPixmap(QtGui.QPixmap().fromImage(widget.graph_image))

    def changeBGColour(self, widget):
        self.bgcolor = QtWidgets.QColorDialog.getColor(title="Select colour for the background of the graph")
        bg = configureImage(widget.graph_image.width(), widget.graph_image.height(), self.gridcolor, self.bgcolor)
        widget.graph_image = bg
        widget.image.setPixmap(QtGui.QPixmap().fromImage(widget.graph_image))

    def changeLineColour(self, widget):
        pencolor = QtWidgets.QColorDialog.getColor(initial=Qt.black, title="Select colour for the lines to be drawn")
        widget.pencolor = pencolor
