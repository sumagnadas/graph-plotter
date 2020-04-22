import pytestqt
from modules.gui import Graph
from PySide2.QtCore import Qt
from time import sleep
from main import ctx, surface, line_color

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

    assert window.graph1.pixelColor(window.p1) == Qt.black,"Line not drawn or Unknown Color"
    assert window.graph1.pixelColor(window.p2) == Qt.black,"Line not drawn or Unknown Color"
