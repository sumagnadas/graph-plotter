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
