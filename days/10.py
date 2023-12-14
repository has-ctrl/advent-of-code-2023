import numpy as np
from shapely import Polygon, MultiPoint

from get_day_input import get_input


data = get_input(day=10).splitlines()


def _find_start() -> tuple[int, int]:
    for i, r in enumerate(data):
        for j, c in enumerate(r):
            if c == "S":
                return i, j


def _find_polygon_coords(outer_coords: list[tuple[int, int]]) -> list[tuple[int, int]]:
    p = Polygon(outer_coords)
    x_min, y_min, x_max, y_max = p.bounds
    x = np.arange(np.floor(x_min), np.ceil(x_max) + 1)
    y = np.arange(np.floor(y_min), np.ceil(y_max) + 1)
    points = MultiPoint(np.transpose([np.tile(x, len(y)), np.repeat(y, len(x))]))
    return [(pt.x, pt.y) for pt in points.intersection(p).geoms]


def _find_loop_coordinates(start_i, start_j) -> list[tuple[int, int]]:
    i, j = start_i, start_j
    location = data[i][j]
    direction = ""
    coordinates = []
    while True:
        match location:
            case "|":
                if direction == "down":
                    i += 1
                else:
                    i -= 1
            case "-":
                if direction == "right":
                    j += 1
                else:
                    j -= 1
            case "L":
                if direction == "down":
                    j += 1
                    direction = "right"
                else:
                    i -= 1
                    direction = "up"
            case "J":
                if direction == "down":
                    j -= 1
                    direction = "left"
                else:
                    i -= 1
                    direction = "up"
            case "7":
                if direction == "up":
                    j -= 1
                    direction = "left"
                else:
                    i += 1
                    direction = "down"
            case "F":
                if direction == "up":
                    j += 1
                    direction = "right"
                else:
                    i += 1
                    direction = "down"
            case "S":
                # Start
                if not direction:
                    j += 1
                    direction = "right"
                # Finish
                else:
                    return coordinates
        location = data[i][j]
        coordinates.append((i, j))


def one() -> int:
    """
    Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting
    position to the point farthest from the starting position?
    """
    i, j = _find_start()
    loop_coordinates = _find_loop_coordinates(i, j)
    return int(len(loop_coordinates) / 2)


def two() -> int:
    """
    Figure out whether you have time to search for the nest by calculating the area within the loop.
    How many tiles are enclosed by the loop?
    """
    i, j = _find_start()
    loop_coordinates = _find_loop_coordinates(i, j)
    all_coordinates = _find_polygon_coords(loop_coordinates)
    return len(all_coordinates) - len(loop_coordinates)


print(f"1. {one()}")
print(f"2. {two()}")
