from get_day_input import get_input


data = get_input(day=1).splitlines()


def one() -> int:
    """
    What is the sum of all of the calibration values?
    """
    total = 0
    for text in data:
        digits = [s for s in text if s.isdigit()]
        total += int(digits[0] + digits[-1])
    return total


def two() -> int:
    """
    What is the sum of all of the calibration values?
    """
    pass


print(f"1. {one()}")
print(f"2. {two()}")
