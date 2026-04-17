import random

def generate_test(x, y):
    color_map = [["white" for j in range(x)] for i in range(y)]

    for i in range(3):
        color_map[i] = ["blue"] * len(color_map[i])

    return color_map

def generate_random_test(x, y):
    color_map = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        color_map.append(row)

    return color_map

color_map = generate_random_test(200, 200)
# color_map = generate_test(200, 200)
# print(*color_map)

def get_color(x, y):
    return color_map[x][y]