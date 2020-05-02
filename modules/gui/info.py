from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
import math
import time


class ExtraInfo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.updateNeeded = True
        layout = QtWidgets.QFormLayout()
        self.str1 = QtWidgets.QLabel('Length of the line:')
        self.distance = QtWidgets.QPushButton('N/A', clicked=self.sidesDialog)
        self.totalSumAngle = QtWidgets.QLabel('N/A')
        self.sides = QtWidgets.QLabel('N/A')
        self.shapeType = QtWidgets.QLabel('N/A')

        self.distance.setStyleSheet('border: transparent')
        layout.addRow(self.str1, self.distance)
        layout.addRow('Sum of all the angles:', self.totalSumAngle)
        layout.addRow('Number of sides:', self.sides)
        layout.addRow('Type of the shape\n(Regular or Irregular):',
                      self.shapeType)

        self.setLayout(layout)
        self.hide()

    def dist(self, points, shapeName):
        x0 = int(points[0][0].text())
        y0 = int(points[0][1].text())
        x3 = int(points[1][0].text())
        y3 = int(points[1][1].text())
        x1 = x0 if x0 >= x3 else x3
        y1 = y0 if y0 >= y3 else y3
        x2 = x0 if x0 < x3 else x3
        y2 = y0 if y0 < y3 else y3
        if shapeName.text() == 'Line':
            dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
        else:
            dist = 'Open'
        return dist if isinstance(dist, str) else f'{dist:.2f}'

    def sumAngle(self, sides, shapeName):
        if shapeName.text() == 'Line':
            sumOfAngles = 0
        else:
            sumOfAngles = (sides - 2) * 180
        return str(sumOfAngles)

    def shapeSides(self, shapeName, points):
        if shapeName.text() == 'Line':
            sides = 1
        else:
            sides = len(points)
        return sides

    def shapeTypeName(self, points):
        dist = []
        try:
            for i in range(0, len(points)):
                x0 = int(points[i][0].text())
                y0 = int(points[i][1].text())
                x3 = int(points[i + 1][0].text())
                y3 = int(points[i + 1][1].text())
                x1 = x0 if x0 >= x3 else x3
                y1 = y0 if y0 >= y3 else y3
                x2 = x0 if x0 < x3 else x3
                y2 = y0 if y0 < y3 else y3
                distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
                dist.append(distance)
        except IndexError:
            x0 = int(points[-1][0].text())
            y0 = int(points[-1][1].text())
            x3 = int(points[0][0].text())
            y3 = int(points[0][1].text())
            x1 = x0 if x0 >= x3 else x3
            y1 = y0 if y0 >= y3 else y3
            x2 = x0 if x0 < x3 else x3
            y2 = y0 if y0 < y3 else y3
            distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
            dist.append(distance)
        return 'Regular' if len(set(dist)) == 1 else 'Irregular'

    def updateInfo(self, points, shapeName, pointNum):
        self.pointNum = pointNum
        self.points = points
        self.distance.setText(self.dist(points, shapeName))
        noOfSides = self.shapeSides(shapeName, points)
        self.totalSumAngle.setText(self.sumAngle(noOfSides, shapeName))
        self.sides.setText(str(noOfSides))
        self.shapeType.setText(self.shapeTypeName(points))

    def sidesDialog(self):
        if True:
            self.sidesLength = QtWidgets.QWidget()
            self.sidesLayout = QtWidgets.QFormLayout()
            self.sidesLayout.addRow(QtWidgets.QLabel(('Lengths of'
                                                      'the lines :-')))
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
                    dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
                    if i + 2 > len(self.points):
                        raise Exception
                    else:
                        self.sidesLayout.addRow(f'P{i+1} to P{i+2} = ',
                                                QtWidgets.QLabel(str(dist)))
            except (IndexError, Exception):
                x0 = int(self.points[-1][0].text())
                y0 = int(self.points[-1][1].text())
                x3 = int(self.points[0][0].text())
                y3 = int(self.points[0][1].text())
                x1 = x0 if x0 >= x3 else x3
                y1 = y0 if y0 >= y3 else y3
                x2 = x0 if x0 < x3 else x3
                y2 = y0 if y0 < y3 else y3
                dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
                self.sidesLayout.addRow(f'P{len(self.points)} to P1 = ',
                                        QtWidgets.QLabel(str(dist)))
            self.sidesLength.setLayout(self.sidesLayout)
            if self.sidesLength.isHidden():
                self.sidesLength.show()
                del self.sidesLayout
            else:
                pass
