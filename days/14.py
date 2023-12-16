from get_day_input import get_input


data = get_input(day=14).splitlines()


def one() -> int:
    """
    Tilt the platform so that the rounded rocks all roll north.
    Afterward, what is the total load on the north support beams?
    """
    transposed_data = [''.join(i) for i in zip(*data)]
    total = 0
    for vertical in transposed_data:
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


def two() -> int:
    """
    Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
