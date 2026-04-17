import math, turtle
import color_map
import julia_math

def color_turtle(t, i, j):
    turtle.colormode(255)
    t.pencolor(color_map.get_color(i, j))

def create_turtle_map(num_x, num_y):
    screen = turtle.Screen()
    screen.setup(width=num_x * 2.5, height=num_y * 2.5)

    turtle.tracer(0)

    turt = turtle.Turtle()
    turt.hideturtle()
    turt.pu()
    
    for i in range(num_y):
        for j in range(num_x):

            turt.goto(2 * (j - (num_x / 2)), 2 * ((num_y / 2) - i))

            color_turtle(turt, i, j)
            turt.dot(3.5)
            
    turtle.update()

    return turt, screen


create_turtle_map(200, 200)
turtle.done()