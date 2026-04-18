import turtle
import mapping

def colored_dot(t, i, j, c_map):
    turtle.colormode(255)
    t.pencolor(mapping.get_color(i, j, c_map))
    t.dot(3)

def create_turtle_map(c, R, max_iteration, num_x, num_y, color1, color2):
    screen = turtle.Screen()
    screen.setup(width=num_x * 1.5, height=num_y * 1.5)

    turtle.tracer(0)

    turt = turtle.Turtle()
    turt.hideturtle()
    turt.pu()

    maps = mapping.get_julia_map(c, R, max_iteration, num_x, num_y, color1, color2)

    iteration_map = maps[0]
    color_map = maps[1]

    #print(iteration_map)
    
    for i in range(num_y):
        for j in range(num_x):

            turt.goto(j - (num_x / 2), (num_y / 2) - i)

            colored_dot(turt, i, j, color_map)
            
    turtle.update()

    turtle.done()

    return turt, screen

c = [-0.835, -.2321]

R = 2
max_iteration = 500

width = 200
height = 200

color1 = [32, 0, 46]
color2 = [255, 105, 180]

create_turtle_map(c, R, max_iteration, width, height, color1, color2)