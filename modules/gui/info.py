from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
import math


class ExtraInfo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.sidesLength = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout()
        self.str1 = QtWidgets.QLabel('Length of the line:')
        self.distance = QtWidgets.QPushButton('N/A', clicked=)
        self.totalSumAngle = QtWidgets.QLabel('N/A')
        self.sides = QtWidgets.QLabel('N/A')
        self.shapeType = QtWidgets.QLabel('N/A')

        self.distance.setStyleSheet('border: transparent')
        layout.addRow(self.str1, self.distance)
        layout.addRow('Sum of all the angles:', self.totalSumAngle)
        layout.addRow('Number of sides:', self.sides)
        layout.addRow('Type of the shape\n(Regular or Irregular):', self.shapeType)

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
            dist = 'N/A'
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
                x3 = int(points[i+1][0].text())
                y3 = int(points[i+1][1].text())
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
        self.distance.setText(self.dist(points, shapeName))
        noOfSides = self.shapeSides(shapeName, points)
        self.totalSumAngle.setText(self.sumAngle(noOfSides, shapeName))
        self.sides.setText(str(noOfSides))
        self.shapeType.setText(self.shapeTypeName(points))

    def sidesDialog(self, pointNum):
        self.sidesLayout = QtWidgets.QFormLayout()
        x = 10
        for i in range(0, pointNum):
            if not (i+1) > pointNum:
                x0 = int(points[i][0].text())
                y0 = int(points[i][1].text())
                x3 = int(points[i-1][0].text())
                y3 = int(points[i-1][1].text())
                x1 = x0 if x0 >= x3 else x3
                y1 = y0 if y0 >= y3 else y3
                x2 = x0 if x0 < x3 else x3
                y2 = y0 if y0 < y3 else y3
                if shapeName.text() == 'Line':
                    dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
                self.sidesLayout.addRow('Lengths of the lines :-')
                self.sidesLayout.addRow(f'P{i} to P{i+1}')
