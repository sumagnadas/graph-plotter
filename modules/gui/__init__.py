from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QFileDialog, QDialog, QCheckBox
from .input import NumInput, ShapeList, PointInput
from .info import ExtraInfo
from os.path import abspath
from modules import geometry
import datetime
import math



class Graph(QtWidgets.QWidget):
    """Class which defines the window of the application"""

    def __init__(self):
        super().__init__()
        ### Some values and widgets needed for the window ###
        self.closedFigure = False
        self.beingTested = False
        self.fileDir = ''
        self.pointNum = 3
        self.image = QtWidgets.QLabel()  # Image container for the graph

        self.pressedOnce = False
        self.points = []
        # Input boxes for the first point of the line
        self.points.append([])
        self.x_coord1 = NumInput()
        self.y_coord1 = NumInput()
        self.points[0].extend([self.x_coord1, self.y_coord1])

        # Input boxes for the second point of the line
        self.points.append([])
        self.x_coord2 = NumInput()  # input boxes for the coordinates
        self.y_coord2 = NumInput()  # input boxes for the coordinates
        self.points[1].extend([self.x_coord2, self.y_coord2])

        ### Buttons for plotting the graph and clearing the text boxes ###

        # 'Draw' Button to draw the line using user-given coordinates
        drawButton = QtWidgets.QPushButton(self.tr("Draw"),
                                           clicked=self.draw)

        # 'Reset' Button to clear everything in the input boxes
        clearButton = QtWidgets.QPushButton(self.tr("Reset"),
                                            clicked=self.clear)

        # Save Button for saving the plotted graph with transparent background
        save = QtWidgets.QPushButton(self.tr("Save this Graph"),
                                     clicked=self.save)

        # Checkbox for choosing whether or not to connect the last and the first point
        closedfigure = QCheckBox("Closed Figure?")
        closedfigure.setCheckState(QtCore.Qt.CheckState.Checked)
        closedfigure.stateChanged.connect(self.shapeNameChange)

        ### Widget containing the main buttons of the application ###

        self.buttonBox = QtWidgets.QDialogButtonBox(QtCore.Qt.Vertical)
        self.buttonBox.addButton(drawButton,
                                 QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(clearButton,
                                 QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(save, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(closedfigure, QtWidgets.QDialogButtonBox.ActionRole)

        #### Layout for the window ###

        self.makeWindowLayout(self.buttonBox)
        self.setImage("resources/graph.png")

    def makeInputLayout(self):
        """ Makes the layout of the input area of the window which
            contains the coordinate inputs and some other widgets"""

        # Layouts for the window
        text = 'Extra Info \N{Black Down-Pointing Triangle}'
        self.inputLayout = QtWidgets.QFormLayout()
        self.coordLayout = QtWidgets.QFormLayout()
        self.scrollArea = QtWidgets.QScrollArea()

        # WIdgets which will be added to the layout of the window
        self.widget = QtWidgets.QWidget()
        self.str = QtWidgets.QLabel('Geometric Figure:')
        self.shapeName = QtWidgets.QLabel('Line')
        self.extraInfo = QtWidgets.QPushButton(text, clicked=self.info)
        self.extraInfo.setToolTip(('Show extra information '
                                   'for the line or shape'))

        # Adding the widgets to the layout of the window
        self.shapeInfo = ExtraInfo()
        self.widget.setLayout(self.coordLayout)
        self.inputLayout.addRow(self.str, self.shapeName)
        self.inputLayout.addRow(self.extraInfo, QtWidgets.QWidget())
        self.inputLayout.addRow(self.shapeInfo)
        self.scrollArea.setWidget(self.widget)
        self.scrollArea.setVerticalScrollBarPolicy(
                                        QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(
                                        QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.inputLayout.addRow(self.scrollArea)

    def makeWindowLayout(self, buttonBox):
        '''Makes the layout of the window'''

        self.pointinput = QtWidgets.QFormLayout()

        # The primary inputs for the coordinates of the lines
        input1 = PointInput('Point1', self.points[0][0], self.points[0][1])
        input2 = PointInput("Point2", self.points[1][0], self.points[1][1])

        # The layout area of the input
        layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        self.addButton = QtWidgets.QPushButton(self.tr('+'), clicked=self.addPoint)
        self.addButton.setToolTip('Add a new point for drawing shapes')

        # The layout area for the main window
        self.windowLayout = layout
        self.windowLayout.addWidget(self.image)
        self.makeInputLayout()
        self.coordLayout.addRow(self.addButton)
        self.coordLayout.addRow(input1)
        self.coordLayout.addRow(input2)
        self.windowLayout.addLayout(self.inputLayout)
        self.windowLayout.addWidget(buttonBox)
        self.setLayout(self.windowLayout)

    def setImage(self, filename):
        '''Set the image for the graph'''

        self.graph_image = QtGui.QImage(abspath(filename))
        self.image.setPixmap(QtGui.QPixmap().fromImage(self.graph_image))

    def draw(self):
        '''Draw a line usself.ing the coordinates of the points
           provided by the user'''

        self.check()
        self.p1 = geometry.Point(int(self.x_coord1.text()),
                                 int(self.y_coord1.text()))
        self.p2 = geometry.Point(int(self.x_coord2.text()),
                                 int(self.y_coord2.text()))
        geometry.plot(self, self.buttonBox.buttons()[3].isChecked())

    def clear(self):
        '''Not to be called by the program
        Resets the input boxes and clear the line(s) on the grid
        When the user presses 'Reset' button'''

        for i in self.points:
            i[0].setText('0')
            i[1].setText('0')

        self.setImage("resources/graph.png")

    def save(self):
        if not self.beingTested:
            caption = self.tr('Choose a filename for saving the graph')
            currentDT = datetime.datetime.now()
            currentTime = currentDT.strftime("%H:%M:%S")
            defFilename = self.fileDir + "graph-" + currentTime + ".png"
            self.dialog = QFileDialog()
            filename = self.dialog.getSaveFileName(self,
            caption,
            abspath('./untitled.png'),
            self.tr('Images (*.png)'))
            self.name = filename[0] if len(filename[0]) > 1 else defFilename
            self.image.grab().toImage().save(self.name, "PNG")
        else:
            self.defFilename = str(self.fileDir) + ("/img.png")
            self.image.grab().toImage().save(str(self.defFilename), "PNG")


    def check(self):
        for i in self.points:
            i[0].setzero()
            i[1].setzero()

    def setSaveFiledir(self, filedir):
        self.fileDir = filedir

    def addPoint(self):
        # Name of the shape
        shapes = {
            3: 'Triangle' if self.buttonBox.buttons()[3].isChecked() else 'Angle',
            4: 'Quadrilateral' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            5: 'Pentagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            6: 'Hexagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            7: 'Septagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            8: 'Octagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            9: 'Enneagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            10: 'Decagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon'
        }

        # Input boxes for the points which are to be added
        x1 = NumInput()
        y1 = NumInput()

        # Extend the points variable to include the new points
        self.points.append([])
        index = len(self.points) - 1
        self.points[index].extend([x1, y1])
        input = PointInput('Point' + str(self.pointNum),
                                self.points[index][0],
                                self.points[index][1])

        self.coordLayout.insertRow(self.coordLayout.rowCount(), input)
        self.shapeInfo.str1.setText('Length of the sides:')
        self.shapeInfo.distance.setStyleSheet('background:solid #F2F3f4')
        self.pointNum += 1
        self.shapeName.setText(shapes.get(index + 1,
                                          ('Undefined shape with {} number of '
                                           'sides').format(index + 1)))
        self.shapeInfo.distance.setText("Open")

    def info(self):
        """
        Show extra info/facts about the shape that has been drawn.
        It will be shown only if the shape is a closed figure.
        """

        if not self.pressedOnce:
            self.extraInfo.setText('Extra Info \N{Black Up-Pointing Triangle}')
            self.shapeInfo.show()
            self.pressedOnce = True
        else:
            self.shapeInfo.hide()
            self.pressedOnce = False
            self.extraInfo.setText(('Extra Info'
                                    '\N{Black Down-Pointing Triangle}'))

    def closeEvent(self, e):
        if hasattr(self.shapeInfo, 'sidesLength'):
            self.shapeInfo.sidesLength.close()
        else:
            e.accept()

    def shapeNameChange(self, e):
        if len(self.points) == 2:
            pass
        else:
            shapes = {
                3: 'Triangle' if self.buttonBox.buttons()[3].isChecked() else 'Angle',
                4: 'Quadrilateral' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
                5: 'Pentagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
                6: 'Hexagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
                7: 'Septagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
                8: 'Octagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
                9: 'Enneagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
                10: 'Decagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon'
            }
            index = len(self.points) - 1
            self.shapeName.setText(shapes.get(index + 1,
                                              ('Undefined shape with {} number of '
                                               'sides').format(index + 1)))
