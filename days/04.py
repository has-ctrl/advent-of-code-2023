from get_day_input import get_input


data = get_input(day=4).splitlines()


def _find_match(card: str) -> set:
    w, m = card.split(":")[1].split("|")
    winning_numbers = set(w.strip().split())
    my_numbers = set(m.strip().split())
    return winning_numbers & my_numbers


def one() -> int:
    """
    Take a seat in the large pile of colorful cards. How many points are they worth in total?
    """
    total = 0
    for card in data:
        match = _find_match(card)
        if match:
            total += 2 ** (len(match)-1)
    return total


def two() -> int:
    """
    Including the original set of scratchcards, how many total scratchcards do you end up with?
    """
    copies = {n: 1 for n, _ in enumerate(data)}
    for i, card in enumerate(data):
        match = _find_match(card)
        if match:
            for j, _ in enumerate(match):
                copies[i + j + 1] += copies[i]
    return sum(copies.values())


print(f"1. {one()}")
print(f"2. {two()}")
