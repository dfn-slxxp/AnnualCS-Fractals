import random

def generate_color_map(x, y):
    color_map = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        color_map.append(row)

    return color_map

color_map = generate_color_map(200, 200)

def get_color(x, y):
    return color_map[x][y]