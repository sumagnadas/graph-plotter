import pytestqt
from modules.gui.layout import QtGui
from modules.gui import Graph
from modules.gui.overloads import filename
from PySide2.QtCore import Qt
from main import ctx, surface, line_color
from os import path


def test_draw(qtbot):
    window = Graph(ctx, surface, line_color)
    window.show()
    qtbot.addWidget(window)

    window.x_coord1.setText('10')
    window.y_coord1.setText('10')
    window.x_coord2.setText('20')
    window.y_coord2.setText('20')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)

    assert window.graph1.pixelColor(window.p1) == Qt.black, ('Line not drawn'
                                                             'or button '
                                                             'not working')
    assert window.graph1.pixelColor(window.p2) == Qt.black, ('Line not drawn'
                                                             'or button '
                                                             'not working')

def test_clear(qtbot):
    window = Graph(ctx, surface, line_color)
    window.show()
    qtbot.addWidget(window)

    window.x_coord1.setText('10')
    window.y_coord1.setText('10')
    window.x_coord2.setText('20')
    window.y_coord2.setText('20')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)

    if window.graph1.pixelColor(window.p1) == Qt.black and window.graph1.pixelColor(window.p2) == Qt.black:
        qtbot.mouseClick(window.buttonBox.buttons()[1], Qt.LeftButton)

        assert window.x_coord1.text() == '0', "Reset button is not working"
        assert window.y_coord1.text() == '0', "Reset button is not working"
        assert window.x_coord2.text() == '0', "Reset button is not working"
        assert window.y_coord2.text() == '0', "Reset button is not working"
    else:
        assert window.graph1.pixelColor(window.p1) == Qt.black, ('Line not drawn'
                                                                 'or button '
                                                                 'not working')
        assert window.graph1.pixelColor(window.p2) == Qt.black, ('Line not drawn'
                                                                 'or button '
                                                                 'not working')
def test_save(qtbot):
    window = Graph(ctx, surface, line_color)
    window.show()
    qtbot.addWidget(window)

    window.x_coord1.setText('10')
    window.y_coord1.setText('10')
    window.x_coord2.setText('20')
    window.y_coord2.setText('20')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)
    window.setSaveFiledir("resources/")

    assert path.exists(path.abspath(filename)) == True, "Save button is not working"