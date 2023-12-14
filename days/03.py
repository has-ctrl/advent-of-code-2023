from get_day_input import get_input


data = get_input(day=3).splitlines()


def _get_surrounding_idx(i: int, j: int) -> list[tuple[int, int]]:
    surroundings = []
    max_x, max_y = len(data) - 1, len(data[0]) - 1
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            search_x, search_y = i + x, j + y
            if 0 <= search_x <= max_x and 0 <= search_y <= max_y:
                if data[search_x][search_y].isdigit():
                    surroundings.append((search_x, search_y))
    return surroundings


def _check_surroundings(i: int, j: int) -> bool:
    max_x, max_y = len(data) - 1, len(data[0]) - 1
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            search_x, search_y = i + x, j + y
            if 0 <= search_x <= max_x and 0 <= search_y <= max_y:
                if not data[search_x][search_y].isdigit() and data[search_x][search_y] != ".":
                    return True
    return False


def one() -> (int, dict[tuple[int, int], int]):
    """
    What is the sum of all of the part numbers in the engine schematic?
    """
    total = 0
    part_numbers_idx = {}
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
                    for j_backwards, _ in enumerate(part_number, 1):
                        part_numbers_idx[(i, j - j_backwards)] = int(part_number)
                    total += int(part_number)
                    adjacent_symbol = False
                part_number = ""
    return total, part_numbers_idx


def two() -> int:
    """
    What is the sum of all of the gear ratios in your engine schematic?
    """
    total = 0
    part_number_idx = one()[1]
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == "*":
                part_numbers = set([part_number_idx[idx] for idx in _get_surrounding_idx(i, j)])
                if len(part_numbers) == 2:
                    p1, p2 = part_numbers
                    total += p1 * p2
    return total


print(f"1. {one()[0]}")
print(f"2. {two()}")
