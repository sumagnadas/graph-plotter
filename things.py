import cairo


class point(object):
    """Class implementation of a point in graph"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y


def set_axes(ctx,axes_color):
    """Draws the axes on the canvas of the cairo object

    Params:-

    ctx - The cairo object for which the axes have to be set up
    r - red value of the colour
    g - green value of the colour
    b - blue value of the colour
    """
    ctx.move_to(0.5, 0)
    ctx.line_to(0.5, 1)
    ctx.close_path()
    ctx.set_source_rgb(axes_color.get_red(), axes_color.get_green(), axes_color.get_blue())
    ctx.set_line_width(0.002)
    ctx.stroke()

    ctx.move_to(0, 0.5)
    ctx.line_to(1, 0.5)
    ctx.close_path()
    ctx.set_source_rgb(axes_color.get_red(), axes_color.get_green(), axes_color.get_blue())
    ctx.set_line_width(0.002)
    ctx.stroke()

    ctx.translate(0.5, 0.5)
    ctx.rotate(270*0.0174533)


def setup_canvas(colour, WIDTH, HEIGHT):
    """Makes the canvas on which the shape/graph will be drawn before output"""

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)

    pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    pat.add_color_stop_rgb(0, colour.get_red(), colour.get_blue(), colour.get_blue())

    ctx.rectangle(0, 0, 1, 1)
    ctx.set_source(pat)
    ctx.fill()
    return ctx,surface

class Geometry(object):
    """Includes all the geometric functions which can used to draw a shape"""

    def draw_line(self, ctx, p1, p2, colour):
        """Draws a line on the canvas"""
        ctx.move_to(p1.x, p1.y)
        ctx.line_to(p2.x, p2.y)
        ctx.close_path()
        ctx.set_source_rgb(colour.get_blue(), colour.get_green(), colour.get_blue())
        ctx.set_line_width(0.005)
        ctx.stroke()

    def draw_triangle(self, ctx, p1, p2, p3, colour):
        """Draws a triangle on the canvas"""
        self.draw_line(ctx, p1, p2, colour)
        self.draw_line(ctx, p2, p3, colour)
        self.draw_line(ctx, p3, p1, colour)

    def draw_quad(self, ctx, p1, p2, p3, p4, colour):
        """Draws a quadrilateral on the canvas"""
        self.draw_line(ctx, p1, p2, colour)
        self.draw_line(ctx, p3, p4, colour)
        self.draw_line(ctx, p2, p3, colour)
        self.draw_line(ctx, p1, p4, colour)

    def draw_polynomial(self, ctx, colour, pointNum, *p):
        """Draws a polynomial with any number of points on the canvas"""
        for i in range(0,pointNum):
            self.draw_line(ctx, p[i], p[i+1], colour)
        draw_line(ctx, p[-2], p[-1], colour)
