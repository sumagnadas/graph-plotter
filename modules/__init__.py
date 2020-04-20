import cairo, colour

def set_axes(ctx,axes_color):
    """Draws the axes on the canvas of the cairo object

    Params:-

    ctx - The cairo object for which the axes have to be set up
    axes_color - Color object for axes
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
    shape = geometry.Geometry()

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
