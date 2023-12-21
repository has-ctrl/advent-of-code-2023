from get_day_input import get_input


data = get_input(day=11).splitlines()


def _find_galaxies(galaxy: list[str]) -> list[tuple[int, int]]:
    galaxy_coordinates = []
    for i, row in enumerate(galaxy):
        for j, c in enumerate(row):
            if c == "#":
                galaxy_coordinates.append((i, j))
    return galaxy_coordinates


def _calc_distance(g1: tuple[int, int], g2: tuple[int, int]) -> int:
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


def _find_empty_rows_and_columns() -> tuple[list[int], list[int]]:
    galaxy_coordinates = _find_galaxies(data)
    all_rows, all_cols = list(range(len(data[0]))), list(range(len(data)))
    empty_rows = [i for i in all_rows if i not in [t[0] for t in galaxy_coordinates]]
    empty_cols = [j for j in all_cols if j not in [t[1] for t in galaxy_coordinates]]
    return empty_rows, empty_cols


def _expand_universe() -> list[str]:
    empty_rows, empty_cols = _find_empty_rows_and_columns()
    expanded_universe = data[:]
    for i, r_idx in enumerate(empty_rows):
        expanded_universe.insert(r_idx + i, "." * len(data))
    for r_idx, _ in enumerate(expanded_universe[:]):
        for j, c_idx in enumerate(empty_cols):
            expanded_universe[r_idx] = expanded_universe[r_idx][:j + c_idx] + "." + expanded_universe[r_idx][j + c_idx:]
    return expanded_universe


def one() -> int:
    """
    Expand the universe, then find the length of the shortest path between every pair of galaxies.
    What is the sum of these lengths?
    """
    total = 0
    expanded_universe = _expand_universe()
    galaxies = _find_galaxies(expanded_universe)
    galaxy_pairs = [(g1, g2) for idx, g1 in enumerate(galaxies) for g2 in galaxies[idx + 1:]]
    for g1, g2 in galaxy_pairs:
        total += _calc_distance(g1, g2)
    return total


def two() -> int:
    """
    Starting with the same initial image, expand the universe according to these new rules,
    then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
    """
    total = 0
    multiplier = 1_000_000 - 1
    galaxies = _find_galaxies(data)
    empty_rows, empty_cols = _find_empty_rows_and_columns()
    galaxy_pairs = [(g1, g2) for idx, g1 in enumerate(galaxies) for g2 in galaxies[idx + 1:]]
    for g1, g2 in galaxy_pairs:
        r_1, r_2, r_count = g1[0], g2[0], 0
        c_1, c_2, c_count = g1[1], g2[1], 0
        for empty_row in empty_rows:
            if r_1 > empty_row >= r_2 or r_2 > empty_row > r_1:
                r_count += 1
        for empty_col in empty_cols:
            if c_1 > empty_col > c_2 or c_2 > empty_col > c_1:
                c_count += 1
        total += _calc_distance(g1, g2) + r_count * multiplier + c_count * multiplier
    return total


print(f"1. {one()}")
print(f"2. {two()}")
