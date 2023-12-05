from get_day_input import get_input


data = get_input(day=5).splitlines()


def _calculate(seeds: list[int]) -> int:
    new_seeds = []
    for line in data[3:]:
        if not line or not line[0].isdigit():
            seeds.extend(new_seeds)
            new_seeds = []
        else:
            dest_start, source_start, range_length = [int(i) for i in line.split()]
            for seed in seeds[:]:
                if source_start <= seed < source_start + range_length:
                    new_seeds.append(dest_start + seed - source_start)
                    seeds.remove(seed)
    return min(seeds + new_seeds)


def one() -> int:
    """
    What is the lowest location number that corresponds to any of the initial seed numbers?
    """
    seeds = [int(s) for s in data[0].split(":")[1].strip().split()]
    return _calculate(seeds)


def two() -> int:
    """
    Consider all of the initial seed numbers listed in the ranges on the first line of the almanac.
    What is the lowest location number that corresponds to any of the initial seed numbers?
    """
    seeds = [int(s) for s in data[0].split(":")[1].strip().split()]
    more_seeds = [list(s) for s in [range(int(seeds[i]), int(seeds[i] + seeds[i + 1])) for i in range(0, len(seeds), 2)]]
    flattened_seeds = [s for l in more_seeds for s in l]
    return _calculate(flattened_seeds)


print(f"1. {one()}")
print(f"2. {two()}")
