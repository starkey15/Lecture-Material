# Turtle graphics

import turtle

def drawSquare(t,x,y,length):
    t.up()
    t.goto(x,y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)
    turtle.done()


def main():
    wn = turtle.Screen()
    joe = turtle.Turtle()
    drawSquare(joe,0,0,250)


if __name__ == "__main__":
    main()
