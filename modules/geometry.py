from PySide2.QtCore import QPoint, Qt
from PySide2 import QtGui


class Point(QPoint):
    """Class implementation of a point in graph"""

    def __init__(self, x=0, y=0):
        x *= 14.85
        x += 299
        y *= 14.85
        y = -y + 299
        super().__init__(x, y)

def plot(window, closedflag):
    graph = QtGui.QImage()
    graph.load("resources/graph.png")
    pen = QtGui.QPen(Qt.black, 5, Qt.SolidLine)
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
    window.shapeInfo.updateInfo(window.points,
                              window.shapeName,
                              window.pointNum,
                              closedflag)
    window.image.setPixmap(QtGui.QPixmap().fromImage(graph))
