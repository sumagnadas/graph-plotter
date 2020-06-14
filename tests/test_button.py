import pytestqt
from modules.gui import Graph, QtWidgets, QtGui
from modules.geometry import dist, Point
from modules import configureImage
from PySide2.QtCore import Qt
from os import path

app = QtWidgets.QApplication()
rect = app.primaryScreen().availableGeometry()
WIDTH = int(rect.width() * (43.92 / 100))
HEIGHT = int(rect.height() * (80.97 / 100))

image = configureImage(WIDTH, HEIGHT)
window = Graph()
window.setImage(image)

def test_coordBox(qtbot):
    window.show()
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

def test_draw(qtbot):
    window.show()

    window.x_coord1.setText('10')
    window.y_coord1.setText('10')
    window.x_coord2.setText('20')
    window.y_coord2.setText('20')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)
    graph = window.image.grab().toImage()
    app.exit()
    for i in range(-20, 20):
        for j in range(-20, 20):
            p = Point(i, j)
            if dist(window.p1, p) + dist(window.p2, p) == dist(window.p1, window.p2):
                assert graph.pixelColor(p) == Qt.black, ('Line not drawn'
                                                             'or button '
                                                             'not working')


def test_save(qtbot, tmpdir_factory):
    window.x_coord1.setText('10')
    window.y_coord1.setText('10')
    window.x_coord2.setText('20')
    window.y_coord2.setText('20')
    qtbot.waitForWindowShown(window)

    window.beingTested = True
    fn = tmpdir_factory.mktemp("data")
    window.setSaveFiledir(str(fn))
    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)
    qtbot.mouseClick(window.buttonBox.buttons()[2], Qt.LeftButton)

    assert fn.join("img.png").check() is True, ('Save button '
                                                         'is not working')

def test_intInput(qtbot):
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
