import math

from get_day_input import get_input


data = get_input(day=6).splitlines()


def _find_intercepts(a: int, b: int, c: int) -> (int, int):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + math.sqrt(discriminant)) / 2 * a
    root2 = (-b - math.sqrt(discriminant)) / 2 * a
    return int(root1), int(root2)


def one() -> int:
    """
    Determine the number of ways you could beat the record in each race.
    What do you get if you multiply these numbers together?
    """
    total = 1
    times = [int(i) for i in data[0].split(":")[1].strip().split()]
    distances = [int(i) for i in data[1].split(":")[1].strip().split()]
    for t, d in zip(times, distances):
        sub_total = 0
        xs = [*range(t+1)]
        for x in xs:
            if (t-x) * x > d:
                sub_total += 1
        total *= sub_total
    return total


def two() -> int:
    """
    How many ways can you beat the record in this one much longer race?
    """
    t = int(data[0].split(":")[1].replace(" ", ""))
    d = int(data[1].split(":")[1].replace(" ", ""))
    max_val, min_val = _find_intercepts(1, -t, d)
    return max_val - min_val


print(f"1. {one()}")
print(f"2. {two()}")
