import pytestqt
from modules.gui import Graph
from PySide2.QtCore import Qt


window = Graph()
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
