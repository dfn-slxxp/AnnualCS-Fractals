import julia_math, json_tool

def interpolate_color(scale, color1, color2):

    r1, g1, b1 = color1[0], color1[1], color1[2]
    r2, g2, b2 = color2[0], color2[1], color2[2]

    r = int(r1 * (1 - scale) + r2 * scale)
    g = int(g1 * (1 - scale) + g2 * scale)
    b = int(b1 * (1 - scale) + b2 * scale)

    return (r, g, b)

def get_julia_map(c, R, max_iteration, x, y, color1, color2):

    if json_tool.check_if_julia_cached_exists(x, y, c[0], c[1], R, max_iteration):
        iteration_map = json_tool.get_julia_from_cache(x, y, c[0], c[1], R, max_iteration)
        
        return [iteration_map, color_maps(iteration_map, max_iteration, color1, color2)]
    else:
        iteration_map = []
        for i in range(y):
            iteration_row = []
            for j in range(x):
                iteration = julia_math.julia_get_iteration(j, i, x, y, c[0], c[1], max_iteration, R)

                iteration_row.append(iteration)

            iteration_map.append(iteration_row)

        maps = [iteration_map, color_maps(iteration_map, max_iteration, color1, color2)]
        json_tool.write_julia_to_cache(x, y, c[0], c[1], R, max_iteration, iteration_map)

        return maps

def color_maps(julia_array, max_iteration, color1, color2):
    color_map = []
    for i in range(len(julia_array)):
        color_row = []
        for j in range(len(julia_array[i])):
            iteration = julia_array[i][j]

            scale = (iteration / max_iteration) ** 0.25
            col = interpolate_color(scale, color1, color2)

            color_row.append(col)

        color_map.append(color_row)

    return color_map

def get_color(x, y, map):
    return map[x][y]