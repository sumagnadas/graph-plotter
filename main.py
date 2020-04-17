from gi import require_foreign, require_version
try:
    require_version('Gtk', '3.0')
    from gi.repository import Gtk
except ValueError:
    print("Cannot import specified version of Gtk")
import things
from tkinter import colorchooser
from colour import Color

require_foreign('cairo')

WIDTH, HEIGHT = 1000, 1000

bg_color = Color(colorchooser.askcolor(title="Choose a color for the background", initialcolor="white")[1])
axes_color = Color(colorchooser.askcolor(title="Choose a color for the axes", initialcolor="black")[1])
line_color = Color(colorchooser.askcolor(title="Choose a color for the line", initialcolor="grey")[1])

p1 = things.point()
p2 = things.point()
p3 = things.point()
p4 = things.point()
shape = things.Geometry()

x1 = int(input("point1 x position:"))/200
y1 = int(input("point1 y position:"))/200

x2 = int(input("\npoint2 x position:"))/200
y2 = int(input("point2 y position:"))/200

x3 = int(input("\npoint3 x position:"))/200
y3 = int(input("point3 y position:"))/200

x4 = int(input("\npoint4 x position:"))/200
y4 = int(input("point4 y position:"))/200

p1.set_coord(x1, y1)
p2.set_coord(x2, y2)
p3.set_coord(x3, y3)
p4.set_coord(x4, y4)

ctx, surface = things.setup_canvas(bg_color, WIDTH, HEIGHT)
things.set_axes(ctx, axes_color)
shape.draw_quad(ctx, p1, p2, p3, p4, line_color)

surface.write_to_png("test.png")
