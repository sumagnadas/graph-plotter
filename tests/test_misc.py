import pytestqt
from modules.gui import QtGui, Graph, QtWidgets
from PySide2.QtCore import Qt
from os import path


def test_closedfigure(qtbot):
    h = QtWidgets.QApplication.instance()
    window = Graph()
    qtbot.addWidget(window)
    qtbot.mouseClick(window.addButton, Qt.LeftButton)
    window.buttonBox.buttons()[4].setCheckState(Qt.CheckState.Unchecked)
    assert window.shapeName.text() == 'Angle', 'Open figures are not being plotted(BUG)'
    window.buttonBox.buttons()[4].setCheckState(Qt.CheckState.Checked)
    assert window.shapeName.text() == 'Triangle', 'Closed figures are not being plotted just after drawing an open figure(BUG)'
    qtbot.mouseClick(window.input[-1].removeButton, Qt.LeftButton)

def test_extrainfo(qtbot):
    h = QtWidgets.QApplication.instance()
    window = Graph()
    qtbot.addWidget(window)
    qtbot.mouseClick(window.extraInfo, Qt.LeftButton)
    assert window.shapeInfo.isHidden() == False, 'Extra Info is not being shown'

def test_removebutton(qtbot):
    h = QtWidgets.QApplication.instance()
    window = Graph()
    oldRowCount = window.coordLayout.rowCount()
    qtbot.mouseClick(window.addButton, Qt.LeftButton)
    qtbot.mouseClick(window.input[-1].removeButton, Qt.LeftButton)
    assert window.coordLayout.rowCount() == oldRowCount, "\"Remove Point\" button is not working"

def test_clear(qtbot):
    h = QtWidgets.QApplication.instance()
    window = Graph()
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

def test_addbutton(qtbot):
    h = QtWidgets.QApplication.instance()
    window = Graph()
    qtbot.mouseClick(window.addButton, Qt.LeftButton)
    assert window.coordLayout.rowCount() == 4, "\"Add Point\" button is not working"
