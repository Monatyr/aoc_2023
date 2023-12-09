from functools import cmp_to_key
from copy import copy


card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "J": 1
}

# hand strength
MAX_STRENGTH = 6

ADV_SOL = False


def get_card_value(card: str):
    # can not use the default in get (conflicting types)
    if card in card_values:
        return card_values.get(card)
    return int(card)


def count_cards_in_hand(hand: list[str]):
    res = dict()
    for card in hand:
        res[card] = res.get(card, 0) + 1
    return res


def fill_jokers(counts: dict()):
    keys = list(counts.keys())
    if len(keys) == 1 and keys[0] == 'J':
        return counts
    
    max_k = -1
    for k, v in counts.items():
        if k != 'J' and v > counts.get(max_k, 0):
            max_k = k
    counts[max_k] += counts.get('J', 0)
    counts['J'] = 0
    return counts



def check_five(counts: dict):
    for count in counts.values():
        if count == 5:
            return True
    return False


def check_four(counts: dict):
    for count in counts.values():
        if count == 4:
            return True
    return False


def check_full_house(counts: dict):
    three, two = False, False
    for count in counts.values():
        if count == 3: three = True
        if count == 2: two = True
    return two and three


# given that full-house was already checked
def check_three(counts: dict):
    for count in counts.values():
        if count == 3:
            return True
    return False


def check_two_pairs(counts: dict):
    pairs = 0
    for count in counts.values():
        if count == 2:
            pairs += 1
    return pairs == 2


def check_pair(counts: dict):
    pairs = 0
    for count in counts.values():
        if count == 2:
            pairs += 1
    return pairs == 1


def hand_strength(hand: dict):
    strength = MAX_STRENGTH
    joker_hand = copy(hand)
    if ADV_SOL:
        print(joker_hand, end=' ')
        joker_hand = fill_jokers(joker_hand)
        print(joker_hand)
    functions = [check_five, check_four, check_full_house, check_three, check_two_pairs, check_pair]
    for f in functions:
        if f(joker_hand):
            return strength
        strength -= 1
    return strength
    

def card_sorting_function(p_1: list, p_2: list):
    h_1, h_2 = p_1[0], p_2[0]
    counts_1, counts_2 = count_cards_in_hand(h_1), count_cards_in_hand(h_2)
    str_1, str_2 = hand_strength(counts_1), hand_strength(counts_2)
    
    if str_1 == str_2:
        for i in range(len(h_1)):
            card_value_1, card_value_2 = get_card_value(h_1[i]), get_card_value(h_2[i])
            if card_value_1 == card_value_2:
                continue
            return -1 if card_value_1 < card_value_2 else 1
    return -1 if str_1 < str_2 else 1


def solution(lines: list[str]):
    res = 0
    sorted_list = sorted(lines, key=cmp_to_key(card_sorting_function))
    for i, pair in enumerate(sorted_list):
        res += int(pair[1]) * (i + 1)
    return res



if __name__ == "__main__":
    filename = "./day7/input.txt"
    with open(filename, 'r') as file:
        lines = list(map(lambda x: x.strip().split(), file.readlines()))

    # part 1
    print(solution(lines))

    # part 2
    ADV_SOL = True
    print(solution(lines))