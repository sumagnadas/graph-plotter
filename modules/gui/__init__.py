from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
from .input import NumInput, ShapeList, PointInput
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

        self.points = {}
        # Input boxes for the first point of the line
        self.points[1] = []
        self.x_coord1 = NumInput()
        self.y_coord1 = NumInput()
        self.points[1].extend([self.x_coord1, self.y_coord1])

        # Input boxes for the second point of the line
        self.points[2] = []
        self.x_coord2 = NumInput()  # input boxes for the coordinates
        self.y_coord2 = NumInput()  # input boxes for the coordinates
        self.points[2].extend([self.x_coord2, self.y_coord2])

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

    def makeInputLayout(self):
        self.inputLayout = QtWidgets.QFormLayout()
        self.dropList = ShapeList()
        self.dropList.activated.connect(self.shape)
        self.inputLayout.addRow(self.dropList)

    def makecoordLayout(self, str, x, y):
        '''Make the layout of the window'''

        inputLayout = QtWidgets.QFormLayout()
        inputLayout.setHorizontalSpacing(10)
        #inputLayout.addRow(dropList)
        inputLayout.addRow(QtWidgets.QLabel(str))
        inputLayout.addRow(QtWidgets.QLabel("X:"), x)
        inputLayout.addRow(QtWidgets.QLabel("Y:"), y)
        self.inputLayout.addRow(inputLayout)
        return self.inputLayout

    def makeWindowLayout(self, buttonBox):
        '''Make the layout of the window'''

        self.pointinput = QtWidgets.QFormLayout()
        input1 = PointInput('Point1', self.points[1][0], self.points[1][1])
        input2 = PointInput("Point2", self.points[2][0], self.points[2][1])
        self.inputLayout1 = QtWidgets.QStackedLayout()
        self.widget = QtWidgets.QWidget()
        layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        self.windowLayout = layout
        self.windowLayout.addWidget(self.image)
        self.makeInputLayout()
        #self.pointinput.addRow(self.makecoordLayout("Point1", self.points[1][0], self.points[1][1]))
        #self.pointinput.addRow(self.makecoordLayout("Point2", self.points[2][0], self.points[2][1]))
        self.pointinput.addRow(self.dropList)
        self.pointinput.addRow(input1)
        self.pointinput.addRow(input2)
        self.widget.setLayout(self.pointinput)
        #self.widget.show()
        self.inputLayout1.insertWidget(0, self.widget)
        self.windowLayout.addLayout(self.inputLayout1)
        self.windowLayout.addWidget(buttonBox)
        self.setLayout(self.windowLayout)

    def setImage(self, filename):
        '''Set the image for the graph'''

        self.graph_image = QtGui.QImage(pt.abspath(filename))
        self.image.setPixmap(QtGui.QPixmap().fromImage(self.graph_image))

    def draw(self):
        '''Draw a line usself.ing the coordinates of the points
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
            if self.dropList.currentText() == 'Line':
                p.drawLine(self.p1.x(), self.p1.y(), self.p2.x(), self.p2.y())
            elif self.dropList.currentText() == 'Triangle':
                self.p3 = geometry.Point(int(self.points[3][0].text()),
                                         int(self.points[3][1].text()))
                p.drawLine(self.p1.x(), self.p1.y(), self.p2.x(), self.p2.y())
                p.drawLine(self.p2.x(), self.p2.y(), self.p3.x(), self.p3.y())
                p.drawLine(self.p3.x(), self.p3.y(), self.p1.x(), self.p1.y())
            p.end()
            self.image.setPixmap(QtGui.QPixmap().fromImage(graph1))
            self.graph1 = graph1

        elif self.save_call:
            self.save_call = False
            currentDT = datetime.datetime.now()
            currentTime = currentDT.strftime("%H:%M:%S")
            filename = self.fileDir + "graph-" + currentTime + ".png"
            self.graph1.save(filename, "PNG")

    def shape(self,i):
        if i == 0:
            print(self.inputLayout.rowCount())
            #self.inputLayout.removeRow(self.inputLayout.rowCount()-1)
            #self.inputLayout.removeRow(self.inputLayout.rowCount()-2)
            #self.inputLayout.removeRow(self.inputLayout.rowCount()-3)
            #self.inputLayout1.insertWidget(2 ,self.widget)
            #self.inputLayout1.setCurrentIndex(0)

        if i == 1:
            self.x1 = NumInput()
            self.y1 = NumInput()
            if 3 not in self.points.keys():
                self.points[3] = [self.x1, self.y1]
                self.makecoordLayout("Point3",self.points[3][0], self.points[3][1])
                self.input = PointInput('Point3', self.points[3][0], self.points[3][1])
                self.input.insertRow(self.widget)

            self.inputLayout1.insertWidget(1, self.input)
            #self.windowLayout.addLayout(self.inputLayout)
            self.inputLayout1.setCurrentIndex(1)
