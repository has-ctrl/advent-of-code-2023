from get_day_input import get_input


data = get_input(day=15).splitlines()


def _hash_algorithm(s: str) -> int:
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def one() -> int:
    """
    Run the HASH algorithm on each step in the initialization sequence. What is the sum of the results?
    """
    total = 0
    for s in data[0].split(','):
        total += _hash_algorithm(s)
    return total


def two() -> int:
    """
    """
    boxes = {i: {} for i in range(256)}
    for s in data[0].split(','):
        if s[-1] == "-":
            label = s[:-1]
            box = _hash_algorithm(label)
            if label in boxes[box]:
                boxes[box].pop(label)
        else:
            label, focal_length = s.split("=")
            box = _hash_algorithm(label)
            boxes[box].update({label: focal_length})
    total = 0
    for i, d in boxes.items():
        for j, (_, f) in enumerate(d.items()):
            total += (i + 1) * (j + 1) * int(f)
    return total


print(f"1. {one()}")
print(f"2. {two()}")
