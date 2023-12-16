from get_day_input import get_input


data = get_input(day=14).splitlines()


def _calculate_load_dynamic(platform: list[str]) -> int:
    total = 0
    for vertical in platform:
        increment = 0
        for i, c in enumerate(vertical):
            load = len(vertical) - i
            match c:
                case ".":
                    increment += 1
                case "O":
                    total += load + increment
                case "#":
                    increment = 0
    return total


def one() -> int:
    """
    Tilt the platform so that the rounded rocks all roll north.
    Afterward, what is the total load on the north support beams?
    """
    transposed_data = [''.join(i) for i in zip(*data)]
    return _calculate_load_dynamic(transposed_data)


def _roll(vertical: str) -> str:
    result = ""
    for chunk in vertical.split("#"):
        result += "".join(sorted(chunk, reverse=True)) + "#"
    return result[:-1]


def _tilt(platform: list[str]) -> list[str]:
    tilted_platform = [''.join(i) for i in zip(*reversed(platform))]
    return [_roll(v) for v in tilted_platform]


def _calculate_load_static(platform: list[str]) -> int:
    total = 0
    for vertical in platform:
        for i, c in enumerate(vertical):
            load = len(vertical) - i
            if c == "O":
                total += load
    return total


def two() -> int:
    """
    Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?
    """
    platform = list(reversed(["".join(reversed(i)) for i in data]))
    platforms_seen = [platform]
    total_cycles = 1_000_000
    for cycle in range(total_cycles):
        for _ in range(4):
            platform = _tilt(platform)
        if platform in platforms_seen:
            loop_start_idx = platforms_seen.index(platform)
            loop_length = cycle - loop_start_idx + 1
            final_idx = (total_cycles - loop_start_idx) % loop_length + loop_start_idx
            north_turned_platform = [''.join(i) for i in zip(*reversed(platforms_seen[final_idx]))]
            return _calculate_load_static(north_turned_platform)
        platforms_seen.append(platform)


print(f"1. {one()}")
print(f"2. {two()}")
