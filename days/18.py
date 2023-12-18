import numpy as np
from shapely import Polygon, MultiPoint

from get_day_input import get_input


data = get_input(day=18).splitlines()


def _find_polygon_coords(outer_coords: list[tuple[int, int]]) -> int:
    p = Polygon(outer_coords)
    x_min, y_min, x_max, y_max = p.bounds
    x = np.arange(np.floor(x_min), np.ceil(x_max) + 1)
    y = np.arange(np.floor(y_min), np.ceil(y_max) + 1)
    points = MultiPoint(np.transpose([np.tile(x, len(y)), np.repeat(y, len(x))]))
    return len([(pt.x, pt.y) for pt in points.intersection(p).geoms])


def one() -> int:
    """
    The Elves are concerned the lagoon won't be large enough; if they follow their dig plan,
    how many cubic meters of lava could it hold?
    """
    coord = (0, 0)
    visited = [coord]
    for command in data:
        direction, amount, color = command.split()
        for i in range(int(amount)):
            if direction == "L":
                coord = coord[0] - 1, coord[1]
            elif direction == "R":
                coord = coord[0] + 1, coord[1]
            elif direction == "U":
                coord = coord[0], coord[1] - 1
            elif direction == "D":
                coord = coord[0], coord[1] + 1
            visited.append(coord)
    return _find_polygon_coords(visited)


def two() -> int:
    """
    """
    pass


print(f"1. {one()}")
print(f"2. {two()}")
