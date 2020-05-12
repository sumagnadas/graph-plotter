#!/usr/bin/env python3
# import the necessary modules
from modules import geometry, configureImage
from modules.gui import Graph, QtWidgets
import sys

# Some necessary variables
app = QtWidgets.QApplication(["Graph Plotter"])  # Name of the application
rect = app.primaryScreen().availableGeometry()
WIDTH = int(rect.width() * (43.92 / 100))
HEIGHT = int(rect.height() * (80.97 / 100))  # Width and height of the graph

# Configures the graph image according to the screen size
configureImage(WIDTH, HEIGHT)

# The code for the main application
if __name__ == "__main__":
    graphPlotter = Graph()  # Make the window
    graphPlotter.show()
    sys.exit(app.exec_())
