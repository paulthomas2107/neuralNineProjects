import turtle
import random


def draw_square(size, turtle_obj):
    turtle_obj.forward(size)
    turtle_obj.left(90)
    turtle_obj.forward(size)
    turtle_obj.left(90)
    turtle_obj.forward(size)
    turtle_obj.left(90)
    turtle_obj.forward(size)


def draw_two_squares(t):
    t.color("red", "blue")
    t.pendown()
    t.begin_fill()
    draw_square(200, t)
    t.end_fill()
    t.penup()
    t.forward(100)
    t.pendown()
    t.begin_fill()
    draw_square(200, t)
    t.end_fill()
    t.penup()


def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.left(216)


def draw_night_sky(t, star_count):
    t.getscreen().bgcolor("#000000")
    t.color("white", "red")
    t.speed(20)
    for _ in range(star_count):
        x, y = random.randint(-300, 300), random.randint(-300, 300)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        draw_star(t, random.randint(5, 125))
        t.end_fill()


def simple_poly():
    turtle.begin_poly()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_poly()
    p = turtle.get_poly()
    turtle.register_shape("SquarePT", p)


def use_square():
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.color("red")
    turtle.shape("SquarePT")


def use_star2():
    turtle.getscreen().onclick(star2)
    star2(turtle.xcor(), turtle.ycor())


def star2(x, y):
    turtle.speed(100)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red", "pink")

    turtle.begin_fill()

    for _ in range(36):
        turtle.forward(150)
        turtle.left(170)

    turtle.end_fill()
    turtle.penup()


t = turtle.Turtle()

t.clear()

# simple_poly()
# use_square()
use_star2()


turtle.done()
