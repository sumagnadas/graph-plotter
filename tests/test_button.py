import pytestqt
from modules.gui import Graph, QtGui, QtWidgets
from modules.geometry import dist, Point
from modules import configureImage
from PySide2.QtCore import Qt, QPoint
from os import path

def test_coordBox(qtbot, qapp):
    print(qapp.instance())
    window = Graph()
    window.setImage(QtGui.QImage("resources/graph.png"))

    str = ('Empty '
           'input box should be taken as zero')

    for i in window.points:
        qtbot.keyClicks(i[0], '')
        qtbot.keyClicks(i[1], '')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)

    for i in window.points:
        assert i[0].text() == '0', str
        assert i[1].text() == '0', str

def test_draw(qtbot, qapp):
    window = Graph()
    window.setImage(QtGui.QImage("resources/graph.png"))

    window.x_coord1.setText('10')
    window.y_coord1.setText('10')
    window.x_coord2.setText('20')
    window.y_coord2.setText('20')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)
    graph = window.graph_image
    for i in range(-20, 20):
        for j in range(-20, 20):
            p = Point(i, j)
            if dist(window.p1, p) + dist(window.p2, p) == dist(window.p1, window.p2):
                assert graph.pixelColor(p) == Qt.black, ('Line not drawn'
                                                             'or button '
                                                             'not working')


def test_save(qtbot, qapp, tmpdir_factory):
    window = Graph()
    window.setImage(QtGui.QImage("resources/graph.png"))

    window.x_coord1.setText('10')
    window.y_coord1.setText('10')
    window.x_coord2.setText('20')
    window.y_coord2.setText('20')
    window.setImage(QtGui.QImage("resources/graph.png"))

    window.beingTested = True
    fn = tmpdir_factory.mktemp("data")
    window.setSaveFiledir(str(fn))
    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)
    qtbot.mouseClick(window.buttonBox.buttons()[2], Qt.LeftButton)

    assert fn.join("img.png").check() is True, ('Save button '
                                                         'is not working')

def test_intInput(qtbot, qapp):
    window = Graph()
    window.setImage(QtGui.QImage("resources/graph.png"))

    qtbot.addWidget(window)
    str = 'Coordinates input box is not supposed take in letter as input'

    for i in window.points:
        qtbot.keyClicks(i[0], 'A')
        qtbot.keyClicks(i[1], 'A')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)

    for i in window.points:
        assert 'A' not in i[0].text(), str
        assert 'A' not in i[1].text(), str

def test_bgchange(qtbot, qapp):
    WIDTH = 599
    HEIGHT = 599
    image = configureImage(WIDTH, HEIGHT, backgroundcolour=Qt.red)

    gridColor = 0
    bgColor = 0
    image =  image.scaled(WIDTH, HEIGHT)
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            p = QPoint(i, j)
            if image.pixelColor(p) == Qt.red:
                bgColor += 1
            else:
                gridColor += 1

    assert (bgColor > gridColor) is True, 'Background colour of the graph is not getting changed'

def test_gridchange(qtbot, qapp):
    WIDTH = 599
    HEIGHT = 599
    image = configureImage(WIDTH, HEIGHT, gridcolour=Qt.red, backgroundcolour=Qt.transparent)

    gridColor = 0
    bgColor = 0
    image =  image.scaled(WIDTH, HEIGHT)
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            p = QPoint(i, j)
            if image.pixelColor(p) == Qt.red:
                gridColor += 1
            else:
                bgColor += 1

    assert (gridColor < bgColor) is True, 'Grid colour of the graph is not getting changed'
