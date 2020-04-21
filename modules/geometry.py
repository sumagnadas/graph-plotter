import cairo
from PySide2.QtCore import QPoint

class point(object):
    """Class implementation of a point in graph"""
    def __init__(self, x=0, y=0):
        self.x = x/200
        self.y = y/200

    def set_coord(self, x, y):
        self.x = x/200
        self.y = y/200

class Point(QPoint):
    """Class implementation of a point in graph"""

    def __init__(self, x=0, y=0):
        x *= 15
        x += 300
        y *= 15
        y = -y + 300
        super().__init__(x, y)

class Geometry(object):
    """Includes all the geometric functions which can used to draw a shape"""

    def draw_line(self, ctx, p1, p2, colour, width):
        """Draws a line on the canvas

        Params:-
            ctx - The cairo.Context object on which the line has to be drawn
            p1, p2,- Consecutive points of the shape
            colour - Colour of the line
        """
        ctx.move_to(p1.x, p1.y)
        ctx.line_to(p2.x, p2.y)
        ctx.close_path()
        ctx.set_source_rgb(colour.get_blue(), colour.get_green(), colour.get_blue())
        ctx.set_line_width(width)
        ctx.stroke()

    def draw_triangle(self, ctx, p1, p2, p3, colour,width):
        """Draws a triangle on the canvas

        Params:-
            ctx - The cairo.Context object on which the shape has to be drawn
            p1, p2, p3 - Consecutive points of the shape
            colour - Colour of the sides
        """

        self.draw_line(ctx, p1, p2, colour,width)
        self.draw_line(ctx, p2, p3, colour,width)
        self.draw_line(ctx, p3, p1, colour,width)

    def draw_quad(self, ctx, p1, p2, p3, p4, colour,width):
        """Draws a quadrilateral on the canvas

        Params:-
            ctx - The cairo.Context object on which the shape has to be drawn
            p1, p2, p3, p4 - Consecutive points of the shape
            colour - Colour of the sides
        """

        self.draw_line(ctx, p1, p2, colour,width)
        self.draw_line(ctx, p3, p4, colour,width)
        self.draw_line(ctx, p2, p3, colour,width)
        self.draw_line(ctx, p1, p4, colour,width)

    def draw_polygon(self, ctx, colour, pointNum, *p):
        """Draws a polygon with 'pointNum' number of points on the canvas
        Params:-
            ctx - The cairo.Context object on which the shape has to be drawn
            colour - Colour of the sides
            pointNum - Number of points supplied to the function
            *p - A list containing the points of the shape
        """

        for i in range(0,pointNum):
            self.draw_line(ctx, p[i-1], p[i], colour,0.005)

    def draw_grid(self,ctx, colour):
        for i in range(-100, 100, 10):
            for j in range(-100, 100, 10):
                p1 = point(i,j)
                p2 = point(i+10,j)
                p3 = point(i+10,j+10)
                p4 = point(i,j+10)
                self.draw_quad(ctx, p1, p2, p3, p4, colour,0.001)

        for i in range(-100, 100, 5):
            for j in range(-100, 100, 5):
                p1 = point(i,j)
                p2 = point(i+10,j)
                p3 = point(i+10,j+10)
                p4 = point(i,j+10)
                self.draw_quad(ctx, p1, p2, p3, p4, colour,0.001)
