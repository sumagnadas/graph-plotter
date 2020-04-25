import pytestqt
from modules.gui import Graph
from main import ctx, surface, line_color
from PySide2.QtCore import Qt
from time import sleep


def test_coordBox(qtbot):
    window = Graph(ctx, surface, line_color)
    window.show()
    qtbot.addWidget(window)
    str = ('Empty '
           'input box should be taken as zero')

    window.x_coord1.setText('')
    window.y_coord1.setText('')
    window.x_coord2.setText('')
    window.y_coord2.setText('')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)

    assert window.x_coord1.text() == '0', str
    assert window.y_coord1.text() == '0', str
    assert window.x_coord2.text() == '0', str
    assert window.y_coord2.text() == '0', str


def test_intInput(qtbot):
    window = Graph(ctx, surface, line_color)
    window.show()
    qtbot.addWidget(window)
    str = 'Coordinates input box is not supposed take in letter input'

    qtbot.keyClicks(window.x_coord1, 'A')
    qtbot.keyClicks(window.y_coord1, 'A')
    qtbot.keyClicks(window.x_coord2, 'A')
    qtbot.keyClicks(window.y_coord2, 'A')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)

    assert 'A' not in window.x_coord1.text(), str
    assert 'A' not in window.y_coord1.text(), str
    assert 'A' not in window.x_coord2.text(), str
    assert 'A' not in window.y_coord2.text(), str
