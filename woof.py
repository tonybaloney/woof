import click
import cairo
import math

COLORS = {
    'black': (0,0,0),
    'brown': (1,.9,.2),
    'yellow': (1,.7, 0),
    'green': (0,1,0),
    'red': (1,0,0),
    'blue': (0,0,1)
}

@click.command()
@click.option('--fur', default='brown', help='Shade of fur.')
@click.option('--breed', prompt='Dog breed',
              help='The breed of dog, e.g. Labrador.')
@click.option('--background', prompt='Background Color', default='black')
def main(fur, breed, background):
    print("Making a {0} {1}...".format(fur, breed))

    WIDTH, HEIGHT = 500, 200

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    ctx.scale(WIDTH, HEIGHT)  

    pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    bg = COLORS[background]
    pat.add_color_stop_rgba(0, *bg, 0.5)
    pat.add_color_stop_rgba(1, *bg, 0.2)

    ctx.rectangle(0, 0, 1, 1)  # fill the background
    ctx.set_source(pat)
    ctx.fill()

    ctx.move_to(0.3, 0.3)
    ctx.line_to(0.9, 0.3)
    ctx.curve_to(0.9, 0.3, 0.95, 0.5, 0.9, 0.8)
    ctx.rel_line_to(-0.4, 0.0)
    ctx.close_path()

    ctx.set_source_rgb(*COLORS['black'])
    ctx.set_line_width(0.01)
    ctx.stroke()

    surface.write_to_png("dog.png")

if __name__ == "__main__":
    main()
