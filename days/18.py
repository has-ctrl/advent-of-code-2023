import numpy as np
from shapely import Polygon, MultiPoint

from get_day_input import get_input


data = get_input(day=18).splitlines()


def _find_polygon_coords(outer_coords: list[tuple[int, int]], n_coords: int) -> int:
    p = Polygon(outer_coords)
    # Shoelace formula and Pick's Theorem... Thanks Google.
    return int(abs(p.area) - 0.5 * n_coords + 1 + n_coords)


def one() -> int:
    """
    The Elves are concerned the lagoon won't be large enough; if they follow their dig plan,
    how many cubic meters of lava could it hold?
    """
    coord = (0, 0)
    visited = [coord]
    n_coords = 1
    for command in data:
        direction, amount, color = command.split()
        if direction == "L":
            coord = coord[0] - int(amount), coord[1]
        elif direction == "R":
            coord = coord[0] + int(amount), coord[1]
        elif direction == "U":
            coord = coord[0], coord[1] - int(amount)
        elif direction == "D":
            coord = coord[0], coord[1] + int(amount)
        visited.append(coord)
        n_coords += int(amount)
    return _find_polygon_coords(visited, n_coords)


def two() -> int:
    """
    Convert the hexadecimal color codes into the correct instructions; if the Elves follow this new dig plan,
    how many cubic meters of lava could the lagoon hold?
    """
    coord = (0, 0)
    visited = [coord]
    n_coords = 1
    for command in data:
        _, _, color = command.split()
        direction = color[-2]
        amount = int(color[2:-2], 16)
        if direction == "2":
            coord = coord[0] - amount, coord[1]
        elif direction == "0":
            coord = coord[0] + amount, coord[1]
        elif direction == "3":
            coord = coord[0], coord[1] - amount
        elif direction == "1":
            coord = coord[0], coord[1] + amount
        visited.append(coord)
        n_coords += int(amount)
    return _find_polygon_coords(visited, n_coords)


print(f"1. {one()}")
print(f"2. {two()}")
