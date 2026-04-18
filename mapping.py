import random
import julia_math

def interpolate_color(scale, color1, color2):

    r1, g1, b1 = color1[0], color1[1], color1[2]
    r2, g2, b2 = color2[0], color2[1], color2[2]

    r = int(r1 * (1 - scale) + r2 * scale)
    g = int(g1 * (1 - scale) + g2 * scale)
    b = int(b1 * (1 - scale) + b2 * scale)

    return (r, g, b)

def generate_julia_map(c, R, max_iteration, x, y, color1, color2):
    iteration_map = []
    color_map = []
    for i in range(y):
        iteration_row = []
        color_row = []
        for j in range(x):
            iteration = julia_math.julia_get_iteration(j, i, x, y, c[0], c[1], max_iteration, R)

            iteration_row.append(iteration)

            scale = (iteration / max_iteration) ** 0.25
            col = interpolate_color(scale, color1, color2)

            color_row.append(col)

        iteration_map.append(iteration_row)
        color_map.append(color_row)

    maps = [iteration_map, color_map]

    return maps

def get_color(x, y, map):
    return map[x][y]