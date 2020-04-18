import cairo

class point(object):
    """Class implementation of a point in graph"""
    def __init__(self, x=0, y=0):
        self.x = x/200
        self.y = y/200

    def set_coord(self, x, y):
        self.x = x/200
        self.y = y/200



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
    ctx.set_line_width(0.005)
    ctx.stroke()

    ctx.move_to(0, 0.5)
    ctx.line_to(1, 0.5)
    ctx.close_path()
    ctx.set_source_rgb(axes_color.get_red(), axes_color.get_green(), axes_color.get_blue())
    ctx.set_line_width(0.005)
    ctx.stroke()
    shape = Geometry()

    ctx.translate(0.5, 0.5)
    shape.draw_grid(ctx, axes_color)
    ctx.scale(1, -1)


def setup_canvas(colour, WIDTH, HEIGHT, alpha=1):
    """Makes the canvas on which the shape/graph will be drawn before output"""

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)

    pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    pat.add_color_stop_rgba(0, colour.get_red(), colour.get_blue(), colour.get_blue(),alpha)
    #pat.add_color_stop_rgba(0, 1, 1, 1,0.8)

    ctx.rectangle(0, 0, 1, 1)
    ctx.set_source(pat)
    ctx.fill()
    return ctx,surface

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
