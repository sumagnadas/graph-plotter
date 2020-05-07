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

    for i in window.points:
        qtbot.keyClicks(i[0], '')
        qtbot.keyClicks(i[1], '')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)

    for i in window.points:
        assert i[0].text() == '0', str
        assert i[1].text() == '0', str


def test_intInput(qtbot):
    window = Graph(ctx, surface, line_color)
    window.show()
    qtbot.addWidget(window)
    str = 'Coordinates input box is not supposed take in letter input'

    for i in window.points:
        qtbot.keyClicks(i[0], 'A')
        qtbot.keyClicks(i[1], 'A')
    qtbot.waitForWindowShown(window)

    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)

    for i in window.points:
        assert 'A' not in i[0].text(), str
        assert 'A' not in i[1].text(), str
