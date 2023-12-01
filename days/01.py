from get_day_input import get_input


data = get_input(day=1).splitlines()
spelled_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


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
    total = 0
    for text in data:
        for word, digit in spelled_digits.items():
            text = text.replace(word, word + str(digit) + word)
        digits = [s for s in text if s.isdigit()]
        total += int(digits[0] + digits[-1])
    return total


print(f"1. {one()}")
print(f"2. {two()}")
