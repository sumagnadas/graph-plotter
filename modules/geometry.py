from PySide2.QtCore import QPoint, Qt
from PySide2 import QtGui
import math
from copy import deepcopy, copy


class Point(QPoint):
    """Class implementation of a point in graph"""

    def __init__(self, x=0, y=0):
        x *= 14.85
        x += 299
        y *= 14.85
        y = -y + 299
        super().__init__(x, y)

def plot(window, closedflag, color):
    graph = copy(window.graph_image)
    pen = QtGui.QPen(color, 5, Qt.SolidLine)
    p = QtGui.QPainter()
    p.begin(graph)
    p.setPen(pen)
    try:
        for i in range(0, len(window.points)):
            p1 = Point(int(window.points[i][0].text()),
                                int(window.points[i][1].text()))
            p2 = Point(int(window.points[i + 1][0].text()),
                                int(window.points[i + 1][1].text()))
            p.drawLine(p1.x(), p1.y(), p2.x(), p2.y())
    except IndexError:
        if closedflag:
            p1 = Point(int(window.points[-1][0].text()),
            int(window.points[-1][1].text()))
            p2 = Point(int(window.points[0][0].text()),
            int(window.points[0][1].text()))
            p.drawLine(p1.x(), p1.y(), p2.x(), p2.y())
        else:
            pass
    p.end()
    graph.save("temp.png", 'PNG')
    window.shapeInfo.updateInfo(window.points,
                              window.shapeName,
                              window.pointNum,
                              closedflag)
    window.image.setPixmap(QtGui.QPixmap().fromImage(graph))

def dist(a, b):
    x0 = int(a.x())
    y0 = int(a.y())
    x3 = int(b.x())
    y3 = int(b.y())
    x1 = x0 if x0 >= x3 else x3
    y1 = y0 if y0 >= y3 else y3
    x2 = x0 if x0 < x3 else x3
    y2 = y0 if y0 < y3 else y3
    dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    return dist
