#!/usr/bin/env python3
# import the necessary modules
from colour import Color
from modules import geometry, set_axes, setup_canvas
from modules.gui import Graph, QtWidgets
import sys

# Some necessary variables
WIDTH, HEIGHT = 600, 600  # Width and height of the graph

# Color objects for having customizable graph colors
bg_color = Color("white")
axes_color = Color("black")
line_color = Color("black")

# Points for drawing the square which is just for testing
p1 = geometry.point()
p2 = geometry.point()
p3 = geometry.point()
p4 = geometry.point()
shape = geometry.Geometry()

# Set the coordinates for the points for the border
p1.set_coord(100, 100)
p2.set_coord(-100, 100)
p3.set_coord(-100, -100)
p4.set_coord(100, -100)

# pycairo objects for making the graph
ctx, surface = setup_canvas(bg_color, WIDTH, HEIGHT, 0)
set_axes(ctx, axes_color)

# The code for the main application
if __name__ == "__main__":
    app = QtWidgets.QApplication(["Graph Plotter"])  # Name of the application
    graphPlotter = Graph(ctx, surface, line_color)  # Make the window
    graphPlotter.show()
    sys.exit(app.exec_())
