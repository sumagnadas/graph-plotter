from PySide2 import QtWidgets, QtGui, QtCore
from .input import NumInput, ShapeList, PointInput
from .info import ExtraInfo
import os.path as pt
from modules import geometry
import datetime
import math

shapes = {
    3: 'Triangle',
    4: 'Quadrilateral',
    5: 'Pentagon',
    6: 'Hexagon',
    7: 'Septagon',
    8: 'Octagon',
    9: 'Enneagon',
    10: 'Decagon'
}


class Graph(QtWidgets.QWidget):
    """Class which defines the window of the application"""

    def __init__(self, ctx, surface, line_color):
        super().__init__()

        self.fileDir = ''
        self.save_call = False
        self.draw_call = False
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

        # Buttons for plotting the graph and clearing the text boxes

        # 'Draw' Button to draw the line using user-given coordinates
        drawButton = QtWidgets.QPushButton(self.tr("Draw"),
                                           clicked=self.draw)
        # 'Reset' Button to clear everything in the input boxes
        clearButton = QtWidgets.QPushButton(self.tr("Reset"),
                                            clicked=self.clear)
        # Save Button for saving the plotted graph with transparent background
        save = QtWidgets.QPushButton(self.tr("Save this Graph"),
                                     clicked=self.save)

        # Widget containing the 'Draw', 'Save this Graph' and 'Reset' button
        self.buttonBox = QtWidgets.QDialogButtonBox(QtCore.Qt.Vertical)
        self.buttonBox.addButton(drawButton,
                                 QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(clearButton,
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
        text = 'Extra Info \N{Black Down-Pointing Triangle}'
        self.inputLayout = QtWidgets.QFormLayout()
        self.coordLayout = QtWidgets.QFormLayout()
        self.scrollArea = QtWidgets.QScrollArea()
        self.widget = QtWidgets.QWidget()
        self.str = QtWidgets.QLabel('Geometric Figure:')
        self.shapeName = QtWidgets.QLabel('Line')
        self.extraInfo = QtWidgets.QPushButton(text, clicked=self.info)
        self.extraInfo.setToolTip(('Show extra information '
                                   'for the line or shape'))
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
        '''Make the layout of the window'''

        self.pointinput = QtWidgets.QFormLayout()
        input1 = PointInput('Point1', self.points[0][0], self.points[0][1])
        input2 = PointInput("Point2", self.points[1][0], self.points[1][1])
        layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        addButton = QtWidgets.QPushButton(self.tr('+'), clicked=self.addPoint)
        addButton.setToolTip('Add a new point for drawing shapes')
        self.windowLayout = layout
        self.windowLayout.addWidget(self.image)
        self.makeInputLayout()
        self.coordLayout.addRow(addButton)
        self.coordLayout.addRow(input1)
        self.coordLayout.addRow(input2)
        self.windowLayout.addLayout(self.inputLayout)
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

        for i in self.points:
            i[0].setText('0')
            i[1].setText('0')
        self.image.setPixmap("resources/graph.png")

    def save(self):
        self.save_call = True
        self.image.update()

    def check(self):
        for i in self.points:
            i[0].setzero()
            i[1].setzero()

    def setSaveFiledir(self, filedir):
        self.fileDir = filedir

    def paintEvent(self, e):
        graph1 = QtGui.QImage()
        if self.draw_call:
            graph1.load("resources/graph.png")
            self.draw_call = False
            pen = QtGui.QPen(QtCore.Qt.black, 5, QtCore.Qt.SolidLine)
            p = QtGui.QPainter()
            p.begin(graph1)
            p.setPen(pen)
            try:
                for i in range(0, len(self.points)):
                    p1 = geometry.Point(int(self.points[i][0].text()),
                                        int(self.points[i][1].text()))
                    p2 = geometry.Point(int(self.points[i + 1][0].text()),
                                        int(self.points[i + 1][1].text()))
                    p.drawLine(p1.x(), p1.y(), p2.x(), p2.y())
            except IndexError:
                p1 = geometry.Point(int(self.points[-1][0].text()),
                                    int(self.points[-1][1].text()))
                p2 = geometry.Point(int(self.points[0][0].text()),
                                    int(self.points[0][1].text()))
                p.drawLine(p1.x(), p1.y(), p2.x(), p2.y())
            p.end()
            self.shapeInfo.updateInfo(self.points,
                                      self.shapeName,
                                      self.pointNum)
            self.image.setPixmap(QtGui.QPixmap().fromImage(graph1))
            self.graph1 = graph1

        elif self.save_call:
            self.save_call = False
            currentDT = datetime.datetime.now()
            currentTime = currentDT.strftime("%H:%M:%S")
            filename = self.fileDir + "graph-" + currentTime + ".png"
            self.graph1.save(filename, "PNG")

    def addPoint(self):
        x1 = NumInput()
        y1 = NumInput()

        self.points.append([])
        index = len(self.points) - 1
        self.points[index].extend([x1, y1])
        self.input = PointInput('Point' + str(self.pointNum),
                                self.points[index][0],
                                self.points[index][1])
        self.coordLayout.insertRow(self.coordLayout.rowCount(), self.input)
        self.shapeInfo.str1.setText('Length of the sides:')
        self.shapeInfo.distance.setStyleSheet('background:solid #F2F3f4')
        self.pointNum += 1
        self.shapeName.setText(shapes.get(index + 1,
                                          ('Undefined shape with {} number of '
                                           'sides').format(index + 1)))

    def info(self):
        if not self.pressedOnce:
            self.extraInfo.setText('Extra Info \N{Black Up-Pointing Triangle}')
            self.shapeInfo.show()
            self.pressedOnce = True
        else:
            self.shapeInfo.hide()
            self.pressedOnce = False
            self.extraInfo.setText(('Extra Info'
                                    '\N{Black Down-Pointing Triangle}'))

    def dist(self):
        x0 = int(self.points[0][0].text())
        y0 = int(self.points[0][1].text())
        x3 = int(self.points[1][0].text())
        y3 = int(self.points[1][1].text())
        x1 = x0 if x0 >= x3 else x3
        y1 = y0 if y0 >= y3 else y3
        x2 = x0 if x0 < x3 else x3
        y2 = y0 if y0 < y3 else y3
        if self.shapeName.text() == 'Line':
            dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
        else:
            dist = 'N/A'
        return dist if isinstance(dist, str) else f'{dist:.2f}'

    def sumAngle(self):
        sides = len(self.points)
        sumOfAngles = (sides - 2) * 180
        return str(sumOfAngles)

    def sides(self):
        if self.shapeName.text() == 'Line':
            sides = str(1)
        else:
            sides = str(len(self.points))
        return sides

    def shapeType(self):
        dist = []
        try:
            for i in range(0, len(self.points)):
                x0 = int(self.points[i][0].text())
                y0 = int(self.points[i][1].text())
                x3 = int(self.points[i + 1][0].text())
                y3 = int(self.points[i + 1][1].text())
                x1 = x0 if x0 >= x3 else x3
                y1 = y0 if y0 >= y3 else y3
                x2 = x0 if x0 < x3 else x3
                y2 = y0 if y0 < y3 else y3
                distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
                dist.append(distance)
        except IndexError:
            x0 = int(self.points[-1][0].text())
            y0 = int(self.points[-1][1].text())
            x3 = int(self.points[0][0].text())
            y3 = int(self.points[0][1].text())
            x1 = x0 if x0 >= x3 else x3
            y1 = y0 if y0 >= y3 else y3
            x2 = x0 if x0 < x3 else x3
            y2 = y0 if y0 < y3 else y3
            distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
            dist.append(distance)
        return 'Regular' if len(set(dist)) == 1 else 'Irregular'

    def closeEvent(self, e):
        self.shapeInfo.sidesLength.close()
