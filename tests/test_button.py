import pytestqt
from modules.gui import QtGui
from modules.gui import Graph
#from modules.gui import Graph.filename
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
    p1Black = window.graph1.pixelColor(window.p1) == Qt.black
    p2Black = window.graph1.pixelColor(window.p2) == Qt.black

    if p1Black and p2Black:
        qtbot.mouseClick(window.buttonBox.buttons()[1], Qt.LeftButton)

        assert window.x_coord1.text() == '0', "Reset button is not working"
        assert window.y_coord1.text() == '0', "Reset button is not working"
        assert window.x_coord2.text() == '0', "Reset button is not working"
        assert window.y_coord2.text() == '0', "Reset button is not working"
    else:
        assert window.graph1.pixelColor(window.p1) == Qt.black, ('Line not '
                                                                 'drawn or '
                                                                 'button not'
                                                                 'working')
        assert window.graph1.pixelColor(window.p2) == Qt.black, ('Line not '
                                                                 'drawn or '
                                                                 'button not'
                                                                 'working')


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
    qtbot.mouseClick(window.buttonBox.buttons()[2], Qt.LeftButton)
    window.dialog.close()
    #window.setSaveFiledir("resources/")

    assert path.exists(path.abspath(window.name)) is True, ('Save button '
                                                         'is not working')
