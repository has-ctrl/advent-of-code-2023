from collections import Counter

from get_day_input import get_input


data = get_input(day=7).splitlines()
strengths = {
    "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}


def one() -> int:
    """
    Find the rank of every hand in your set. What are the total winnings?
    """
    scores = []
    for row in data:
        hand, bid = row.split()
        counter = Counter(hand).most_common()

        if counter[0][1] == 5:
            hand_type = 6  # Five of a Kind
        elif counter[0][1] == 4:
            hand_type = 5  # Four of a kind
        elif counter[0][1] == 3 and counter[1][1] == 2:
            hand_type = 4  # Full House
        elif counter[0][1] == 3:
            hand_type = 3  # Three of a Kind
        elif counter[0][1] == 2 and counter[1][1] == 2:
            hand_type = 2  # Two Pair
        elif counter[0][1] == 2:
            hand_type = 1  # One Pair
        else:
            hand_type = 0  # High Card

        score_order = [hand_type, *[strengths[i] for i in hand]]
        scores.append((score_order, bid))

    total = 0
    for i, (_, bid) in enumerate(sorted(scores)):
        total += (i + 1) * int(bid)
    return total


def two() -> int:
    """
    How many ways can you beat the record in this one much longer race?
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
