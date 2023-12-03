from get_day_input import get_input


data = get_input(day=3).splitlines()


def _check_surroundings(i: int, j: int) -> bool:
    max_x, max_y = len(data) - 1, len(data[0]) - 1
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            search_x, search_y = i + x, j + y
            if 0 <= search_x <= max_x and 0 <= search_y <= max_y:
                if not data[search_x][search_y].isdigit() and data[search_x][search_y] != ".":
                    return True
    return False


def one() -> int:
    """
    What is the sum of all of the part numbers in the engine schematic?
    """
    total = 0
    for i, row in enumerate(data):
        part_number = ""
        adjacent_symbol = False
        for j, c in enumerate(row):
            if c.isdigit():
                part_number += c
                if not adjacent_symbol:
                    adjacent_symbol = _check_surroundings(i, j)
            if not c.isdigit() or j == len(row) - 1:
                if adjacent_symbol:
                    total += int(part_number)
                    adjacent_symbol = False
                part_number = ""
    return total


print(f"1. {one()}")
