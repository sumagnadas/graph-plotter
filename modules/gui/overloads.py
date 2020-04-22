import datetime
from .layout import QtGui, Qt, QtWidgets


class NumInput(QtWidgets.QLineEdit):
    """Class which defines the input boxes for the coordinates"""
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(100)
        self.setMaxLength(4)
        onlyInt = QtGui.QIntValidator(-300, 300)
        self.setValidator(onlyInt)
        self.setText("0")

    def setzero(self):
        if self.text() == '':
            self.setText('0')


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
        filename = "graph-"+currentTime+".png"
        self.graph.save(filename, "PNG")
