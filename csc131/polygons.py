import turtle


def square(t: turtle.Turtle, length: int) -> None:
    """
    Draw a square of a given length
    :param t: an instance of a Turtle used to render the square
    :param length: length of one side of the rendered square
    :return: None
    """
    for count in range(4):
        t.forward(length)
        t.left(90)

def hexagon(t: turtle.Turtle, length: int) -> None:
    """
    Draw a square of a given length
    :param t: an instance of a Turtle used to render the hexagon
    :param length: length of one side of the rendered hexagon
    :return: None
    """
    for count in range(6):
        t.forward(length)
        t.left(60)

def triangle(t: turtle.Turtle, length: int) -> None:
    """
    Draw a square of a given length
    :param t: an instance of a Turtle used to render the triangle
    :param length: length of one side of the rendered triangle
    :return: None
    """
    for count in range(3):
        t.forward(length)
        t.left(120)

def octagon(t: turtle.Turtle, length: int) -> None:
    """
    Draw a square of a given length
    :param t: an instance of a Turtle used to render the octagon
    :param length: length of one side of the rendered octagon
    :return: None
    """
    for count in range(8):
        t.forward(length)
        t.left(45)


# stop sign shape w/o STOP word -- fixed border, need to fix
def draw_polygon(t: turtle.Turtle, length: int, sides: int) -> None:
    for count in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.penup()
    t.goto(5,15)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for count in range(sides):
        t.forward(length-10)
        t.left(360/sides)
    t.end_fill()
    turtle.done()

turtle.speed(10)
draw_polygon(turtle, 50, 10)
