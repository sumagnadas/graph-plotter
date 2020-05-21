import pytestqt
from modules.gui import QtGui
from modules.gui import Graph, QtWidgets
from PySide2.QtCore import Qt
from os import path


window = Graph()
def test_extrainfo(qtbot):
    qtbot.addWidget(window)
    qtbot.mouseClick(window.extraInfo, Qt.LeftButton)
    assert window.shapeInfo.isHidden() == False, 'Extra Info is not being shown'

def test_closedfigure(qtbot):
    qtbot.addWidget(window)
    qtbot.mouseClick(window.addButton, Qt.LeftButton)
    window.buttonBox.buttons()[3].setCheckState(Qt.CheckState.Unchecked)
    assert window.shapeName.text() == 'Angle', 'Open figures are not being plotted(BUG)'
    window.buttonBox.buttons()[3].setCheckState(Qt.CheckState.Checked)
    assert window.shapeName.text() == 'Triangle', 'Closed figures are not being plotted just after drawing an open figure(BUG)'
