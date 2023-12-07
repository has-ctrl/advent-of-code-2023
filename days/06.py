from get_day_input import get_input


data = get_input(day=6).splitlines()


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
    Consider all of the initial seed numbers listed in the ranges on the first line of the almanac.
    What is the lowest location number that corresponds to any of the initial seed numbers?
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
