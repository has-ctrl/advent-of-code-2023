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


def _expand_universe() -> list[str]:
    galaxy_coordinates = _find_galaxies(data)
    all_rows, all_cols = list(range(len(data[0]))), list(range(len(data)))
    empty_rows = [i for i in all_rows if i not in [t[0] for t in galaxy_coordinates]]
    empty_cols = [j for j in all_cols if j not in [t[1] for t in galaxy_coordinates]]

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
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")