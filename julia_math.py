import sys

sys.setrecursionlimit(5000)

def julia_get_point_as_rgb(x, y, width, height, cx, cy):
    R = 2
    max_iteration = 500
    
    zx = (x / (width - 1)) * 3 - 1.5
    zy = 1.5 - (y / (height - 1)) * 3


    scale = julia(zx, zy, cx, cy, R, 0, max_iteration)

    # color = (0, int(255 - (255 * scale / max_iteration)), 255)

    # return color

    t = scale / max_iteration
    t = t ** 0.3

    if t == max_iteration:
        return (5, 10, 90)

    if t < 0.5:
        u = t / 0.5
        r = 0
        g = int(40 * u)
        b = int(80 + 175 * u)
    else:
        u = (t - 0.5) / 0.5
        r = int(180 * u)
        g = int(40 + 215 * u)
        b = 255

    return (r, g, b)

def julia(zx, zy, cx, cy, R, iteration, max_iteration):

    if iteration == max_iteration:
        return max_iteration
    
    if zx * zx + zy * zy >= R**2:
        return iteration

    xtemp = zx * zx - zy * zy + cx
    zy = 2 * zx * zy + cy
    zx = xtemp

    return julia(zx, zy, cx, cy, R, iteration + 1, max_iteration)