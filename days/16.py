from get_day_input import get_input


data = get_input(day=16).splitlines()


def _move(x: int, y: int, direction: str):
    min_x = min_y = 0
    max_x, max_y = len(data[0]) - 1, len(data) - 1
    new_xs, new_ys = [], []
    match data[y][x], direction:
        case "\\", "up": new_ds = ["left"]
        case "\\", "right": new_ds = ["down"]
        case "\\", "down": new_ds = ["right"]
        case "\\", "left": new_ds = ["up"]
        case "/", "up": new_ds = ["right"]
        case "/", "right": new_ds = ["up"]
        case "/", "down": new_ds = ["left"]
        case "/", "left": new_ds = ["down"]
        case "-", "up" | "down": new_ds = ["left", "right"]
        case "|", "left" | "right": new_ds = ["up", "down"]
        case _: new_ds = [direction]

    for i, d in enumerate(new_ds[:]):
        if d == "up" and y > min_y:
            new_xs.append(x)
            new_ys.append(y - 1)
        elif d == "right" and x < max_x:
            new_xs.append(x + 1)
            new_ys.append(y)
        elif d == "down" and y < max_y:
            new_xs.append(x)
            new_ys.append(y + 1)
        elif d == "left" and x > min_x:
            new_xs.append(x - 1)
            new_ys.append(y)
        else:
            new_xs.append(None)
            new_ys.append(None)
            new_ds[i] = None
            continue
        new_ds[i] = d
    return new_xs, new_ys, new_ds


def one(start_x: int = 0, start_y: int = 0, start_d: str = "right") -> int:
    """
    With the beam starting in the top-left heading right, how many tiles end up being energized?
    """
    xs, ys = [start_x], [start_y]
    directions = [start_d]
    visited_tiles = [(start_x, start_y, start_d)]
    energized_tiles = {(start_x, start_y)}
    while True:
        if not directions:
            return len(energized_tiles)
        temp_xs, temp_ys, temp_ds = [], [], []
        for x, y, d in zip(xs[:], ys[:], directions[:]):
            new_xs, new_ys, new_ds = _move(x, y, d)
            for new_x, new_y, new_d in zip(new_xs, new_ys, new_ds):
                if new_d and (new_x, new_y, new_d) not in visited_tiles:
                    visited_tiles.append((new_x, new_y, new_d))
                    energized_tiles.add((new_x, new_y))
                    temp_xs.append(new_x)
                    temp_ys.append(new_y)
                    temp_ds.append(new_d)
        xs, ys, directions = temp_xs, temp_ys, temp_ds


def two() -> int:
    """
    Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive
    blocks in the same direction, what is the least heat loss it can incur?
    """
    min_x, min_y = 0, 0
    max_x, max_y = len(data[0]) - 1, len(data) - 1
    edges = [(x, min_y) for x in range(max_x)] + \
            [(min_x, y) for y in range(max_y)] + \
            [(x, max_y) for x in range(max_x)] + \
            [(max_x, y) for y in range(max_y)]
    max_score = 0
    for x, y in set(edges):
        if x == min_x:
            score = one(x, y, "right")
        elif x == max_x:
            score = one(x, y, "left")
        elif y == min_x:
            score = one(x, y, "down")
        else:
            score = one(x, y, "up")
        if score:
            max_score = score if score > max_score else max_score
    return max_score


print(f"1. {one()}")
print(f"2. {two()}")
