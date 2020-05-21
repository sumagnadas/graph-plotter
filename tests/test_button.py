import pytestqt
from modules.gui import Graph, QtWidgets, QtGui
from modules.geometry import dist, Point
from PySide2.QtCore import Qt
from os import path

app = QtWidgets.QApplication()
window = Graph()
def test_draw(qtbot):
    window.show()

    window.x_coord1.setText('10')
    window.y_coord1.setText('10')
    window.x_coord2.setText('20')
    window.y_coord2.setText('20')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)
    graph = window.image.grab().toImage()
    
    for i in range(-20, 20):
        for j in range(-20, 20):
            p = Point(i, j)
            if dist(window.p1, p) + dist(window.p2, p) == dist(window.p1, window.p2):
                assert graph.pixelColor(p) == Qt.black, ('Line not drawn'
                                                             'or button '
                                                             'not working')


def test_clear(qtbot):
    window.x_coord1.setText('10')
    window.y_coord1.setText('10')
    window.x_coord2.setText('20')
    window.y_coord2.setText('20')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[1], Qt.LeftButton)

    assert window.x_coord1.text() == '0', "Reset button is not working"
    assert window.y_coord1.text() == '0', "Reset button is not working"
    assert window.x_coord2.text() == '0', "Reset button is not working"
    assert window.y_coord2.text() == '0', "Reset button is not working"


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
def test_addbutton(qtbot):
    qtbot.mouseClick(window.addButton, Qt.LeftButton)
    assert window.coordLayout.rowCount() == 4, "\"Add Point\" button is not working"

def test_removebutton(qtbot):
    oldRowCount = window.coordLayout.rowCount()
    qtbot.mouseClick(window.addButton, Qt.LeftButton)
    qtbot.mouseClick(window.input[-1].removeButton, Qt.LeftButton)
    assert window.coordLayout.rowCount() == oldRowCount, "\"Remove Point\" button is not working"
