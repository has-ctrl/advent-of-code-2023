from get_day_input import get_input


data = get_input(day=10).splitlines()


def _find_start() -> tuple[int, int]:
    for i, r in enumerate(data):
        for j, c in enumerate(r):
            if c == "S":
                return i, j


def one() -> int:
    """
    Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting
    position to the point farthest from the starting position?
    """
    i, j = _find_start()
    location = data[i][j]
    direction = ""
    steps = 0
    while True:
        match location:
            case "|":
                if direction == "down":
                    i += 1
                else:
                    i -= 1
            case "-":
                if direction == "right":
                    j += 1
                else:
                    j -= 1
            case "L":
                if direction == "down":
                    j += 1
                    direction = "right"
                else:
                    i -= 1
                    direction = "up"
            case "J":
                if direction == "down":
                    j -= 1
                    direction = "left"
                else:
                    i -= 1
                    direction = "up"
            case "7":
                if direction == "up":
                    j -= 1
                    direction = "left"
                else:
                    i += 1
                    direction = "down"
            case "F":
                if direction == "up":
                    j += 1
                    direction = "right"
                else:
                    i += 1
                    direction = "down"
            case "S":
                # Start
                if not direction:
                    j += 1
                    direction = "right"
                # Finish
                else:
                    return int(steps / 2)
        location = data[i][j]
        steps += 1


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
