import random
import julia_math

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
        color_map.append(row),

    return color_map


def generate_julia_map(x, y, c):
    color_map = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(julia_math.julia_get_point_as_rgb(j, i, x, y, c[0], c[1]))
        color_map.append(row)

    # print(color_map)
    return color_map

# color_map = generate_julia_map(200, 200)
# color_map = generate_random_test(200, 200)
# color_map = generate_test(200, 200)
# print(*color_map)

def get_color(x, y, map):
    return map[x][y]