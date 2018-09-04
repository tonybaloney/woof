import click
import cairo


COLORS = {
    'black': (0,0,0),
    'brown': (1,.9,.2),
    'yellow': (1,.7, 0),
    'green': (0,1,0),
    'red': (1,0,0),
    'blue': (0,0,1)
}

BREEDS = {
     # breed = (BACK, BETWEEN LEGS, LEG LENGTH, LEG WIDTH, TAIL LENGTH, HEAD SIZE)
    'shitzu': (0.2, 0.01, 0.1, 0.01, 0.02, 0.2),
    'labrador': (0.4, 0.05, 0.4, 0.02, 0.2, 0.2),
}

@click.command()
@click.option('--fur', default='brown', help='Shade of fur.')
@click.option('--breed', prompt='Dog breed',
              help='The breed of dog, e.g. Labrador.')
@click.option('--background', prompt='Background Color', default='black')
def main(fur, breed, background):
    print("Making a {0} {1}...".format(fur, breed))
    WIDTH, HEIGHT = 500, 200
    BACK_LENGTH, LEG_GAP, LEG_LENGTH, LEG_WIDTH, TAIL_LENGTH, HEAD_SIZE = BREEDS[breed]

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    START = (1-BACK_LENGTH-0.2-(LEG_WIDTH*4)-(LEG_GAP*3), 1-LEG_LENGTH-0.3)

    ctx.scale(WIDTH, HEIGHT)  

    pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    bg = COLORS[background]
    pat.add_color_stop_rgba(0, *bg, 0.5)
    pat.add_color_stop_rgba(1, *bg, 0.2)

    ctx.rectangle(0, 0, 1, 1)
    ctx.set_source(pat)
    ctx.fill()

    ctx.move_to(*START)
    ctx.rel_line_to(BACK_LENGTH, 0.0)
    cox = ctx.get_current_point()
    ctx.curve_to(0.9, START[1], 0.95, 0.5, 0.9, 0.6)  # backside
    ctx.rel_line_to(-0, 0.4)
    ctx.rel_line_to(-LEG_WIDTH, 0)
    ctx.rel_line_to(-0, -LEG_LENGTH)
    ctx.rel_line_to(-LEG_GAP, 0.0)
    ctx.rel_line_to(-0, LEG_LENGTH)
    ctx.rel_line_to(-LEG_WIDTH, 0)
    ctx.rel_line_to(-0, -LEG_LENGTH)
    ctx.rel_line_to(-0.3, 0.0)  # belly - rub me!!
    ctx.rel_line_to(-0, LEG_LENGTH)
    ctx.rel_line_to(-LEG_WIDTH, 0)
    ctx.rel_line_to(-0, -LEG_LENGTH)
    ctx.rel_line_to(-LEG_GAP, 0.0)
    ctx.rel_line_to(-0, LEG_LENGTH)
    ctx.rel_line_to(-LEG_WIDTH, 0)
    ctx.rel_line_to(-0, -LEG_LENGTH)
    ctx.rel_line_to(-LEG_GAP*2, -0.1)
    pos = ctx.get_current_point()
    ctx.curve_to(pos[0]-HEAD_SIZE, pos[1]-.1, pos[0]-HEAD_SIZE, pos[1]-.4, *START)
    fur = cairo.SolidPattern(*COLORS[fur],.4)
    ctx.set_source(fur)
    ctx.fill()
    ctx.close_path()

    surface.write_to_png("dog.png")

if __name__ == "__main__":
    main()
