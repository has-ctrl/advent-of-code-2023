from get_day_input import get_input


data = get_input(day=2).splitlines()


def one() -> int:
    """
    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes,
    and 14 blue cubes. What is the sum of the IDs of those games?
    """
    total = 0
    for i, game in enumerate(data):
        is_possible = True
        for cube_set in game.split(': ')[1].split(';'):
            for cube_color in cube_set.split(','):
                match cube_color.split():
                    case [n, "red"]: is_possible = int(n) <= 12 and is_possible
                    case [n, "green"]: is_possible = int(n) <= 13 and is_possible
                    case [n, "blue"]: is_possible = int(n) <= 14 and is_possible
        if is_possible:
            total += (i + 1)
    return total


def two() -> int:
    """
    For each game, find the minimum set of cubes that must have been present.
    What is the sum of the power of these sets?
    """
    pass


print(f"1. {one()}")
print(f"2. {two()}")
