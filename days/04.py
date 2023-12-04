from get_day_input import get_input


data = get_input(day=4).splitlines()


def one() -> int:
    """
    Take a seat in the large pile of colorful cards. How many points are they worth in total?
    """
    total = 0
    for card in data:
        w, m = card.split(":")[1].split("|")
        winning_numbers = set(w.strip().split())
        my_numbers = set(m.strip().split())
        match = winning_numbers & my_numbers
        if match:
            total += 2 ** (len(match)-1)
    return total


def two() -> int:
    """
    Including the original set of scratchcards, how many total scratchcards do you end up with?
    """
    pass


print(f"1. {one()}")
