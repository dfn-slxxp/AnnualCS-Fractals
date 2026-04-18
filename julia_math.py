import sys
import mapping

sys.setrecursionlimit(5000)

def julia_get_iteration(x, y, width, height, cx, cy, max_iteration, R):
    
    zx = (x / (width - 1)) * 3 - 1.5
    zy = 1.5 - (y / (height - 1)) * 3

    iteration = julia(zx, zy, cx, cy, R, 0, max_iteration)

    return iteration

def julia(zx, zy, cx, cy, R, iteration, max_iteration):

    if iteration == max_iteration:
        return max_iteration
    
    if zx * zx + zy * zy >= R**2:
        return iteration

    xtemp = zx * zx - zy * zy + cx
    zy = 2 * zx * zy + cy
    zx = xtemp

    return julia(zx, zy, cx, cy, R, iteration + 1, max_iteration)