from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
from .input import NumInput
import os.path as pt
from modules import geometry
import datetime


class Graph(QtWidgets.QWidget):
    """Class which defines the window of the application"""

    def __init__(self, ctx, surface, line_color):
        super().__init__()

        self.fileDir = ''
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
        self.drawButton = QtWidgets.QPushButton(self.tr("Draw"),
                                                clicked=self.draw)
        # 'Reset' Button to clear everything in the input boxes
        self.clearButton = QtWidgets.QPushButton(self.tr("Reset"),
                                                 clicked=self.clear)
        # Save Button for saving the plotted graph with transparent background
        save = QtWidgets.QPushButton(self.tr("Save this Graph"),
                                     clicked=self.save)

        # Widget containing the 'Draw', 'Save this Graph' and 'Reset' button
        self.buttonBox = QtWidgets.QDialogButtonBox(Qt.Vertical)
        self.buttonBox.addButton(self.drawButton,
                                 QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.clearButton,
                                 QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(save, QtWidgets.QDialogButtonBox.ActionRole)

        # Layout for the window
        self.makeWindowLayout(self.buttonBox)
        self.setImage("resources/graph.png")

        # Some extra values for the implementation of the GUi
        self.ctx = ctx
        self.surface = surface
        self.line_color = line_color

    def makeGraphLayout(self, str, x, y):
        '''Make the layout of the window'''
        inputLayout = QtWidgets.QFormLayout()
        inputLayout.setHorizontalSpacing(10)
        inputLayout.addRow(QtWidgets.QLabel(str))
        inputLayout.addRow(QtWidgets.QLabel("X:"), x)
        inputLayout.addRow(QtWidgets.QLabel("Y:"), y)
        self.windowLayout.addLayout(inputLayout)

    def makeWindowLayout(self, buttonBox):
        '''Make the layout of the window'''

        layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        self.windowLayout = layout
        self.windowLayout.addWidget(self.image)
        self.makeGraphLayout("Point1", x=self.x_coord1, y=self.y_coord1)
        self.makeGraphLayout("Point2", x=self.x_coord2, y=self.y_coord2)
        self.windowLayout.addWidget(buttonBox)
        self.setLayout(self.windowLayout)

    def setImage(self, filename):
        '''Set the image for the graph'''

        self.graph_image = QtGui.QImage(pt.abspath(filename))
        self.image.setPixmap(QtGui.QPixmap().fromImage(self.graph_image))

    def draw(self):
        '''Draw a line using the coordinates of the points
           provided by the user'''

        self.check()
        self.p1 = geometry.Point(int(self.x_coord1.text()),
                                 int(self.y_coord1.text()))
        self.p2 = geometry.Point(int(self.x_coord2.text()),
                                 int(self.y_coord2.text()))
        self.draw_call = True
        self.image.repaint()

    def clear(self):
        '''Not to be called by the program
        Resets the input boxes and clear the line(s) on the grid
        When the user presses 'Reset' button'''

        self.x_coord1.setText("0")
        self.y_coord1.setText("0")
        self.x_coord2.setText("0")
        self.y_coord2.setText("0")
        self.image.setPixmap("resources/graph.png")

    def save(self):
        self.save_call = True
        self.image.update()

    def check(self):
        self.x_coord1.setzero()
        self.y_coord1.setzero()
        self.x_coord2.setzero()
        self.y_coord2.setzero()

    def setSaveFiledir(self, filedir):
        self.fileDir = filedir

    def paintEvent(self, e):
        graph1 = QtGui.QImage()

        if self.draw_call:
            graph1.load("resources/graph.png")
            self.draw_call = False
            pen = QtGui.QPen(Qt.black, 5, Qt.SolidLine)
            p = QtGui.QPainter()
            p.begin(graph1)
            p.setPen(pen)
            p.drawLine(self.p1.x(), self.p1.y(), self.p2.x(), self.p2.y())
            p.end()
            self.image.setPixmap(QtGui.QPixmap().fromImage(graph1))
            self.graph1 = graph1

        elif self.save_call:
            self.save_call = False
            currentDT = datetime.datetime.now()
            currentTime = currentDT.strftime("%H:%M:%S")
            filename = self.fileDir + "graph-" + currentTime + ".png"
            self.graph1.save(filename, "PNG")
