from modules import geometry
from PySide2.QtGui import QImage, QPainter, QPen, QPainter
from PySide2.QtCore import Qt


def draw_quad(p, p1, p2, p3, p4):
    """Draws a quadrilateral on the QImage object

    Params:-
        p - The QPainter object which is drawing the shape
        p1, p2, p3, p4 - Consecutive points of the shape
    """

    p.drawLine(p1, p2)
    p.drawLine(p3, p4)
    p.drawLine(p2, p3)
    p.drawLine(p1, p4)

def draw_grid(p, colour=Qt.black):
    """Draws a grid on the QImage object
    Params:-
        p - The QPainter object which is drawing the shape
        colour - The colour of the the grid
    """
    p.setPen(QPen(colour, 1))
    for i in range(-20, 20, 2):
        for j in range(-20, 20, 2):
            p1 = geometry.Point(i, j)
            p2 = geometry.Point(i + 10, j)
            p3 = geometry.Point(i + 10, j + 10)
            p4 = geometry.Point(i, j + 10)
            draw_quad(p, p1, p2, p3, p4)

    for i in range(-20, 20, 1):
        for j in range(-20, 20, 1):
            p1 = geometry.Point(i, j)
            p2 = geometry.Point(i + 10, j)
            p3 = geometry.Point(i + 10, j + 10)
            p4 = geometry.Point(i, j + 10)
            draw_quad(p, p1, p2, p3, p4)

def configureImage(width, height, gridcolour=None, backgroundcolour=None):
    """Configures the image for the graph that will be shown in the
    application
    Params:-
        width -  Width of the screen on which the application will be shown
        height - Height of the screen on which the application will be shown
    """
    gridcolour = gridcolour if not gridcolour is None else Qt.black

    p1 = geometry.Point(0, -20)
    p2 = geometry.Point(0, 20)
    p3 = geometry.Point(20, 0)
    p4 = geometry.Point(-20, 0)
    p5 = geometry.Point(20, 20)
    p6 = geometry.Point(-20, 20)
    p7 = geometry.Point(-20, -20)
    p8 = geometry.Point(20, -20)
    graphImage = QImage(width, height, QImage.Format_ARGB32)
    
    if not backgroundcolour is None:
        graphImage.fill(backgroundcolour)
    pen = QPen(gridcolour, 3)
    p = QPainter()
    p.begin(graphImage)
    p.setPen(pen)
    p.drawLine(p1, p2)
    p.drawLine(p3, p4)

    pen = QPen(gridcolour, 2)
    p.setPen(pen)
    p.drawLine(p5, p6)
    p.drawLine(p6, p7)
    p.drawLine(p7, p8)
    p.drawLine(p8, p5)

    draw_grid(p, gridcolour)
    p.end()
    return graphImage
