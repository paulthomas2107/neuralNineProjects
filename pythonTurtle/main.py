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


def draw_night_sky(t):
    t.getscreen().bgcolor("#000000")
    t.color("white", "red")
    t.speed(10)
    for _ in range(50):
        x, y = random.randint(-300, 300), random.randint(-300, 300)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        draw_star(t, random.randint(5, 25))
        t.end_fill()


t = turtle.Turtle()

draw_night_sky(t)

turtle.done()


