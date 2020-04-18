from gi import require_foreign
from gi import repository
import things
from tkinter import colorchooser, Tk
from colour import Color
require_foreign('cairo')
import gui

WIDTH, HEIGHT = 600, 600
window = Tk()
window.withdraw()
transparent = Color
bg_color = Color(colorchooser.askcolor(title="Choose a color for the background", initialcolor="white")[1])
axes_color = Color(colorchooser.askcolor(title="Choose a color for the axes", initialcolor="black")[1])
line_color = Color(colorchooser.askcolor(title="Choose a color for the line", initialcolor="grey")[1])

p1 = things.point()
p2 = things.point()
p3 = things.point()
p4 = things.point()
shape = things.Geometry()

"""x1 = int(input("point1 x position:"))/200
y1 = int(input("point1 y position:"))/200

x2 = int(input("\npoint2 x position:"))/200
y2 = int(input("point2 y position:"))/200

x3 = int(input("\npoint3 x position:"))/200
y3 = int(input("point3 y position:"))/200

x4 = int(input("\npoint4 x position:"))/200
y4 = int(input("point4 y position:"))/200"""

p1.set_coord(0, 0)
p2.set_coord(0, 10)
p3.set_coord(10, 10)
p4.set_coord(10, 0)

ctx, surface = things.setup_canvas(bg_color, WIDTH, HEIGHT, 0)
things.set_axes(ctx, axes_color)
shape.draw_quad(ctx, p1, p2, p3, p4, line_color)

app = gui.QtWidgets.QApplication(["Graph Plotter"])
graphPlotter = gui.Graph(ctx, surface, line_color)
graphPlotter.resize(WIDTH, HEIGHT)
surface.write_to_png("graph.png")
graphPlotter.setImage("graph.png")
graphPlotter.show()
gui.sys.exit(app.exec_())
