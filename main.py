#!/usr/bin/env python3
# import the necessary modules
from gi import require_foreign

from tkinter import colorchooser, Tk
from colour import Color
require_foreign('cairo')
from modules import gui, geometry, set_axes, setup_canvas

#Hide an extra window which opened along with the color chooser dialog
window = Tk()
window.withdraw()

# Some necessary variables
WIDTH, HEIGHT = 600, 600 # Width and height of the graph

# Color objects for having customizable graph colors
bg_color = Color(colorchooser.askcolor(title="Choose a color for the background", initialcolor="white")[1])
axes_color = Color(colorchooser.askcolor(title="Choose a color for the axes", initialcolor="black")[1])
line_color = Color(colorchooser.askcolor(title="Choose a color for the line", initialcolor="grey")[1])

#Points for drawing the square which is just for testing
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
back_ctx, back_surface = setup_canvas(bg_color, WIDTH, HEIGHT, 0)
set_axes(ctx, axes_color)
set_axes(back_ctx, axes_color)

#The code for the main application
app = gui.QtWidgets.QApplication(["Graph Plotter"])# Name of the application
graphPlotter = gui.Graph(ctx, surface, line_color, [back_ctx, surface])# Make the window
surface.write_to_png("graph.png")# Save the basic graph that will be shown on the application
graphPlotter.setImage("graph.png")# Set the Graph for the application
graphPlotter.show()
gui.sys.exit(app.exec_())
