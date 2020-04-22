from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from .overloads import NumInput


class Graph(QtWidgets.QWidget):
    """Class which defines the window of the application"""

    def __init__(self, ctx, surface, line_color):
        super().__init__()

        self.save_call = False
        self.draw_call = False
        self.image = QtWidgets.QLabel()  # Image container for the graph

        # Input boxes for the first point of the line
        self.x_coord1 = NumInput()
        self.y_coord1 = NumInput()

        # Input boxes for the second point of the line
        self.x_coord2 = NumInput()  # input boxes for the coordinates
        self.y_coord2 = NumInput()  # input boxes for the coordinates

        # Buttons for plotting the graph and clearing the text boxes

        # 'Draw' Button to draw the line using user-given coordinates
        self.drawButton = QtWidgets.QPushButton(self.tr("Draw"), clicked=self.draw)
        # 'Reset' Button to clear everything in the input boxes
        clear = QtWidgets.QPushButton(self.tr("Reset"), clicked=self.clear)
        # Save Button for saving the plotted graph with transparent background
        save = QtWidgets.QPushButton(self.tr("Save this Graph"),
                                     clicked=self.save)

        # Widget containing the 'Draw', 'Save this Graph' and 'Reset' button
        self.buttonBox = QtWidgets.QDialogButtonBox(Qt.Vertical)
        self.buttonBox.addButton(self.drawButton, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(clear, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(save, QtWidgets.QDialogButtonBox.ActionRole)

        # Layout for the window
        self.makeWindowLayout(self.buttonBox)
        self.setImage("resources/graph.png")

        # Some extra values for the implementation of the GUi
        self.ctx = ctx
        self.surface = surface
        self.line_color = line_color

    from .buttonfunc import clear, draw, save, check
    from .layout import makeWindowLayout, makeGraphLayout, setImage
    from .overloads import paintEvent
