import pytestqt
from modules.gui import QtGui
from modules.gui import Graph, QtWidgets
from PySide2.QtCore import Qt
from os import path

app = QtWidgets.QApplication()
window = Graph()
def test_draw(qtbot):
    window.show()
    #qtbot.addWidget(window)

    window.x_coord1.setText('10')
    window.y_coord1.setText('10')
    window.x_coord2.setText('20')
    window.y_coord2.setText('20')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)

    assert window.image.grab().toImage().pixelColor(window.p1) == Qt.black, ('Line not drawn'
                                                             'or button '
                                                             'not working')
    assert window.image.grab().toImage().pixelColor(window.p2) == Qt.black, ('Line not drawn'
                                                             'or button '
                                                             'not working')


def test_clear(qtbot):
    #window = Graph(ctx, surface, line_color)
    #window.show()
    #qtbot.addWidget(window)

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
    #window = Graph(ctx, surface, line_color)
    #window.show()
    #qtbot.addWidget(window)

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
