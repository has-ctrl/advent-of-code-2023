import numpy as np

from get_day_input import get_input


data = get_input(day=9).splitlines()


def _calc_sequence(values: list[int], part2: bool = False) -> int:
    total = 0
    while True:
        if not any(values):
            return total
        elif part2:
            total -= values[-1]
        else:
            total += values[-1]
        values = np.diff(values)


def one() -> int:
    """
    Analyze your OASIS report and extrapolate the next value for each history. What is the sum of these extrapolated values?
    """
    total = 0
    for history in data:
        values = [int(v) for v in history.split()]
        total += _calc_sequence(values)
    return total


def two() -> int:
    """
    Analyze your OASIS report again, this time extrapolating the previous value for each history.
    What is the sum of these extrapolated values?
    """
    total = 0
    for history in data:
        values = [int(v) for v in history.split()]
        total += _calc_sequence(values[::-1])
    return total


print(f"1. {one()}")
print(f"2. {two()}")
