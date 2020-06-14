from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QFileDialog, QDialog, QCheckBox
from .input import NumInput, PointInput
from .info import ExtraInfo
from .customizations import CustomizeMenu
from os.path import abspath, isfile
from os import remove
from modules import geometry
import datetime
import math


class Graph(QtWidgets.QWidget):
    """Class which defines the window of the application"""

    def __init__(self):
        super().__init__()
        ### Some values and widgets needed for the window ###
        self.pencolor = QtCore.Qt.black
        self.closedFigure = False
        self.beingTested = False
        self.fileDir = ''
        self.pointNum = 2
        self.image = QtWidgets.QLabel()  # Image container for the graph
        self.name = "resources/graph.png"
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
        drawButton.setIcon(QtGui.QIcon("resources/icons/draw_icon.png"))

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

        menuButton =  QtWidgets.QPushButton(self.tr("Customize"))
        menuButton.setMenu(CustomizeMenu("Customize", self,
                                         self.image.size().width(),
                                         self.image.size().height(),
                                         parent=menuButton))
        ### Widget containing the main buttons of the application ###
        self.buttonBox = QtWidgets.QDialogButtonBox(QtCore.Qt.Vertical)
        self.buttonBox.addButton(drawButton,
                                 QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(clearButton,
                                 QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(save, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(menuButton, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(closedfigure, QtWidgets.QDialogButtonBox.ActionRole)

        ### Layout for the window ###
        self.setStyleSheet('QMenu::item:selected{background: transparent; color: #000099}')
        self.makeWindowLayout(self.buttonBox)

        # Set the shortcut keys
        self.setShortcuts()

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
                                   'for the line or shape(Ctrl+Shift+E)'))

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
        self.input = [input1, input2]
        # The layout area of the input
        layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        self.addButton = QtWidgets.QPushButton(self.tr('+'), clicked=self.addPoint)
        self.addButton.setToolTip('Add a new point for drawing shapes(Ctrl+Shift+A)')

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

        self.graph_image = QtGui.QImage(abspath(filename)) if not isinstance(filename, QtGui.QImage) else filename
        self.image.setPixmap(QtGui.QPixmap().fromImage(self.graph_image))

    def draw(self):
        '''Draw a line using the coordinates of the points
           provided by the user'''

        self.check()
        self.p1 = geometry.Point(int(self.x_coord1.text()),
                                 int(self.y_coord1.text()))
        self.p2 = geometry.Point(int(self.x_coord2.text()),
                                 int(self.y_coord2.text()))
        geometry.plot(self, self.buttonBox.buttons()[4].isChecked(), self.pencolor)

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
            self.dialog = QFileDialog()
            filename = self.dialog.getSaveFileName(self,
                caption,
                abspath('./untitled.png'),
                self.tr('Images (*.png)'))
            if filename[1]:
                self.name = filename[0]
                self.graph_image.save(self.name, 'PNG')
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
        """Adds an input for the user to put in coordinates for another point"""

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
        self.pointNum += 1
        self.points.append([])
        index = len(self.points) - 1
        self.points[index].extend([x1, y1])
        self.input.append(PointInput('Point' + str(self.pointNum),
                                self.points[index][0],
                                self.points[index][1]))

        self.input[-1].removeButton.setIcon(QtGui.QIcon(QtGui.QPixmap("resources/icons/removeButton.png")))
        self.input[-1].removeButton.show()
        input = self.input[-1]
        self.input[-1].removeButton.clicked.connect(lambda: self.removePoint(input))
        self.input[-1].removeButton.setShortcut("Ctrl+Del")
        self.input[-1].removeButton.setToolTip("Removes the input area for this point(Ctrl+Del[+Space])")
        self.coordLayout.insertRow(self.coordLayout.rowCount(), self.input[-1])
        self.shapeInfo.str1.setText('Length of the sides:')
        self.shapeInfo.distance.setStyleSheet('background:solid #F2F3f4')
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
        self.extraInfo.setShortcut("Ctrl+Shift+E")
    def closeEvent(self, e):
        if hasattr(self.shapeInfo, 'sidesLength'):
            self.shapeInfo.sidesLength.close()
        else:
            e.accept()

    def shapeNameChange(self, e):
        shapes = {
            2: 'Line',
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

    def setShortcuts(self):
        """Sets the shortcut for most of the buttons"""

        self.buttonBox.buttons()[0].setShortcut("Return")
        self.buttonBox.buttons()[1].setShortcut("Ctrl+R")
        self.buttonBox.buttons()[2].setShortcut("Ctrl+S")
        self.addButton.setShortcut('Ctrl+Shift+A')
        self.extraInfo.setShortcut("Ctrl+Shift+E")

    def removePoint(self, input):
        """Removes an input area as per the user"""

        # Name of the figures
        figures = {
            2: 'Line',
            3: 'Triangle' if self.buttonBox.buttons()[3].isChecked() else 'Angle',
            4: 'Quadrilateral' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            5: 'Pentagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            6: 'Hexagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            7: 'Septagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            8: 'Octagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            9: 'Enneagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon',
            10: 'Decagon' if self.buttonBox.buttons()[3].isChecked() else 'Open Polygon'
        }

        # Remove the input are from the program and and the GUI
        index = self.input.index(input)
        text = input.layout.itemAt(0).layout().itemAt(0).widget().text()
        input.hide()
        self.points.remove(input.xy())
        self.input.pop(index)
        self.coordLayout.removeRow(index+1)

        # Change the name of the point
        j = 0
        for i in range(1, len(self.input) + 1):
            self.input[j].layout.itemAt(0).layout().itemAt(0).widget().setText(f"Point{i}")
            j += 1

        self.pointNum -= 1
        index = len(self.points)

        # Change the shape name in the GUI
        self.shapeName.setText(figures.get(index,
                                          ('Undefined shape with {} number of '
                                           'sides').format(index + 1)))
        if self.shapeName.text() == 'Line':
            self.shapeInfo.distance.setText("N/A")
            self.shapeInfo.distance.setStyleSheet('border: transparent')
    def closeEvent(self, e):
        remove("temp.png") if isfile("temp.png") else None
