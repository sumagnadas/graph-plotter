from PySide2.QtCore import QPoint


class Point(QPoint):
    """Class implementation of a point in graph"""

    def __init__(self, x=0, y=0):
        x *= 14.85
        x += 299
        y *= 14.85
        y = -y + 299
        super().__init__(x, y)

def plot(p, points):
    try:
        for i in range(0, len(points)):
            p1 = Point(int(points[i][0].text()),
                                int(points[i][1].text()))
            p2 = Point(int(points[i + 1][0].text()),
                                int(points[i + 1][1].text()))
            p.drawLine(p1.x(), p1.y(), p2.x(), p2.y())
    except IndexError:
        p1 = Point(int(points[-1][0].text()),
                            int(points[-1][1].text()))
        p2 = Point(int(points[0][0].text()),
                            int(points[0][1].text()))
        p.drawLine(p1.x(), p1.y(), p2.x(), p2.y())
