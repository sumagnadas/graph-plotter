from modules import geometry
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QPoint, Qt

from .overloads import NumInput

class Graph(QtWidgets.QWidget):
    """Class which defines the window of the application"""

    def __init__(self, ctx, surface, line_color):
        super().__init__()

        self.save_call = False
        self.draw_call = False
        self.image = QtWidgets.QLabel()# Image container for the graph

        #Input boxes for the first point of the line
        self.x_coord1 = NumInput()
        self.y_coord1 = NumInput()

        #Input boxes for the second point of the line
        self.x_coord2 = NumInput()# input boxes for the coordinates
        self.y_coord2 = NumInput()# input boxes for the coordinates

        #Buttons for plotting the graph and clearing the text boxes
        draw = QtWidgets.QPushButton(self.tr("Draw"))# 'Draw' Button to draw the line using coordinates of the point provided by the user
        clear = QtWidgets.QPushButton(self.tr("Clear"))# 'Reset' Button to clear everything in the input boxes
        save = QtWidgets.QPushButton(self.tr("Save this Graph"),clicked=self.save)

        #Widget containing the 'Draw', 'Save this Graph' and 'Reset' button
        buttonBox = QtWidgets.QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(draw, QtWidgets.QDialogButtonBox.AcceptRole)
        buttonBox.addButton(clear, QtWidgets.QDialogButtonBox.RejectRole)
        buttonBox.addButton(save, QtWidgets.QDialogButtonBox.ActionRole)

        #Connect the buttons to their respective functions so when one of the buttons is pressed, the respective function will be called
        buttonBox.accepted.connect(self.draw)
        buttonBox.rejected.connect(self.clear)

        #Layout for the window
        self.makeWindowLayout(buttonBox)
        self.setImage("graph.png")

        # Some extra values for the implementation of the GUi
        self.ctx = ctx
        self.surface = surface
        self.line_color = line_color

    from .buttonfunc import clear, draw, save, check
    from .layout import makeWindowLayout, makeGraphLayout, setImage
    from .overloads import paintEvent
