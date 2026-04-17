import turtle
import color_map

def colored_dot(t, i, j, c_map):
    turtle.colormode(255)
    t.pencolor(color_map.get_color(i, j, c_map))
    t.dot(3)

def create_turtle_map(num_x, num_y, c):
    screen = turtle.Screen()
    screen.setup(width=num_x * 1.5, height=num_y * 1.5)

    turtle.tracer(0)

    turt = turtle.Turtle()
    turt.hideturtle()
    turt.pu()

    c_map = color_map.generate_julia_map(num_x, num_y, c)
    
    for i in range(num_y):
        for j in range(num_x):

            turt.goto(j - (num_x / 2), (num_y / 2) - i)

            colored_dot(turt, i, j, c_map)
            
    turtle.update()

    turtle.done()

    return turt, screen

c = [-0.835, -.2321]
width = 600
height = 600
create_turtle_map(width, height, c)