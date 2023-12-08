from collections import Counter

from get_day_input import get_input


data = get_input(day=7).splitlines()


def _calculate_hand_type(hand_list: list[tuple[str, int]]) -> int:
    if hand_list[0][1] == 5:
        return 6  # Five of a Kind
    elif hand_list[0][1] == 4:
        return 5  # Four of a kind
    elif hand_list[0][1] == 3 and hand_list[1][1] == 2:
        return 4  # Full House
    elif hand_list[0][1] == 3:
        return 3  # Three of a Kind
    elif hand_list[0][1] == 2 and hand_list[1][1] == 2:
        return 2  # Two Pair
    elif hand_list[0][1] == 2:
        return 1  # One Pair
    else:
        return 0  # High Card


def one() -> int:
    """
    Find the rank of every hand in your set. What are the total winnings?
    """
    strengths = {
        "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
    }
    scores = []
    for row in data:
        hand, bid = row.split()
        hand_list = Counter(hand).most_common()
        hand_type = _calculate_hand_type(hand_list)
        score_order = [hand_type, *[strengths[i] for i in hand]]
        scores.append((score_order, bid))
    return sum([(i + 1) * int(bid) for i, (_, bid) in enumerate(sorted(scores))])


def two() -> int:
    """
    Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
    """
    strengths = {
        "A": 14, "K": 13, "Q": 12, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1
    }
    scores = []
    for row in data:
        hand, bid = row.split()
        hand_list = Counter(hand).most_common()
        if "J" not in hand:
            hand_type = _calculate_hand_type(hand_list)
        else:
            hand_type = 0
            for k, v in hand_list:
                hand_list_copy = Counter(hand.replace('J', k)).most_common()
                new_hand_type = _calculate_hand_type(hand_list_copy)
                hand_type = new_hand_type if new_hand_type > hand_type else hand_type
        score_order = [hand_type, *[strengths[i] for i in hand]]
        scores.append((score_order, bid))
    return sum([(i + 1) * int(bid) for i, (_, bid) in enumerate(sorted(scores))])


print(f"1. {one()}")
print(f"2. {two()}")
