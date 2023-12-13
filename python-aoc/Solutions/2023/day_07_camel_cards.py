from advent import get_input, solution_timer
from functools import cmp_to_key

order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
order2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

high = 1
one_pair = 2
two_pair = 3
three_of_a_kind = 4
full_house = 5
four_of_a_kind = 6
five_of_a_kind = 7


def get_rank(hand):
    set_hand = set(hand)
    match len(set_hand):
        case 1:
            return five_of_a_kind
        case 2:
            if hand.count(hand[0]) == 4 or hand.count(hand[0]) == 1:
                return four_of_a_kind
            return full_house
        case 3:
            if any([hand.count(x) == 3 for x in set_hand]):  # 3 of a kind
                return three_of_a_kind
            return two_pair
        case 4:
            return one_pair
        case _:
            return high


def get_rank_wildcard(hand):
    if "J" in hand:
        return max([get_rank(hand.replace("J", x)) for x in order2 if x != "J"])
    else:
        return get_rank(hand)


def gen_compare(rank_func, order):
    def compare(hand1, hand2):
        hand1 = hand1[0]
        hand2 = hand2[0]
        if rank_func(hand1) > rank_func(hand2):
            return 1
        elif rank_func(hand1) < rank_func(hand2):
            return -1
        else:
            for i in range(5):
                if order.index(hand1[i]) > order.index(hand2[i]):
                    return -1
                elif order.index(hand1[i]) < order.index(hand2[i]):
                    return 1
        return 0

    return compare


@solution_timer(2023, 7, 1)
def part_one(inp):
    hb = []
    for hand in inp:
        han, bet = hand.split()
        hb.append((han, int(bet)))

    p1_compare = gen_compare(get_rank, order)

    hb.sort(key=cmp_to_key(p1_compare))
    return sum([(idx + 1) * hand[1] for idx, hand in enumerate(hb)])


@solution_timer(2023, 7, 2)
def part_two(inp):
    hb = []
    for hand in inp:
        han, bet = hand.split()
        hb.append((han, int(bet)))

    p2_compare = gen_compare(get_rank_wildcard, order2)

    hb.sort(key=cmp_to_key(p2_compare))
    ans = 0
    for idx, hand in enumerate(hb):
        ans += (idx + 1) * hand[1]
    return ans


if __name__ == "__main__":
    inp = get_input(2023, 7)
    part_one(inp)
    part_two(inp)
