from advent import get_input, solution_timer, submit
from functools import cmp_to_key

order  = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
order2  = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J']

@solution_timer(2023, 7, 1)
def part_one(inp):

    hb= []
    for hand in inp:
        han, bet = hand.split()
        hb.append((han, int(bet)))


    def get_typ(hand):
        shand = set(hand)

        if len(shand) == 1:
            print(hand, "5 of a kind")
            return 7
        if len(shand) == 2:
            if hand.count(hand[0]) == 4 or hand.count(hand[0]) == 1:
                print(hand, "4 of a kind")
                return 6 # 4 of a kind
            return 5 # full house
        if len(shand) == 3:
            print(hand, "3 of a kind")
            if any([hand.count(x) == 3 for x in shand]): # 3 of a kind
                return 4
            # 2 pair
            print(hand, "2 pair")
            return 3 # check case
        if len(shand) == 4:
            print(hand, "1 pair")
            return 2 # 1 pair
        print(hand, "high card")
        return 1

    
    def compare(hand1, hand2):
        hand1 = hand1[0]
        hand2 = hand2[0]
        if get_typ(hand1) > get_typ(hand2):
            return 1
        elif get_typ(hand1) < get_typ(hand2):
            return -1
        else:
            for i in range(5):
                if order.index(hand1[i]) > order.index(hand2[i]):
                    return -1
                elif order.index(hand1[i]) < order.index(hand2[i]):
                    return 1
        return 0
    
    hb.sort(key=cmp_to_key(compare))
        
    print(hb)
    ans = 0
    for idx, hand in enumerate(hb):
        ans += (idx + 1) * hand[1]
    return ans


fiveoc = 7
fouroc = 6
fullh = 5
threec = 4
twopair = 3
onepair = 2
highc = 1

@solution_timer(2023, 7, 2)
def part_two(inp):
    hb= []
    for hand in inp:
        han, bet = hand.split()
        hb.append((han, int(bet)))


    def get_typ(hand):
        shand = set(hand)
        ans = 0
        if "J" in shand:
            for i in range(len(order2)-1):
                nhand = hand
                for j in range(len(nhand)):
                    if nhand[j] == "J":
                        nhand = nhand[:j] + order2[i] + nhand[j+1:]
                ans = max(ans, get_typ(nhand))
            return ans
        else:
            if len(shand) == 1:
                print(hand, "5 of a kind")
                return 7
            if len(shand) == 2:
                if hand.count(hand[0]) == 4 or hand.count(hand[0]) == 1:
                    print(hand, "4 of a kind")
                    return 6 # 4 of a kind
                return 5 # full house
            if len(shand) == 3:
                print(hand, "3 of a kind")
                if any([hand.count(x) == 3 for x in shand]): # 3 of a kind
                    return 4
                # 2 pair
                print(hand, "2 pair")
                return 3 # check case
            if len(shand) == 4:
                print(hand, "1 pair")
                return 2 # 1 pair
            print(hand, "high card")
            return 1

    
    def compare(hand1, hand2):
        hand1 = hand1[0]
        hand2 = hand2[0]
        if get_typ(hand1) > get_typ(hand2):
            return 1
        elif get_typ(hand1) < get_typ(hand2):
            return -1
        else:
            for i in range(5):
                if order2.index(hand1[i]) > order2.index(hand2[i]):
                    return -1
                elif order2.index(hand1[i]) < order2.index(hand2[i]):
                    return 1
        return 0
    
    hb.sort(key=cmp_to_key(compare))
        
    ans = 0
    for idx, hand in enumerate(hb):
        ans += (idx + 1) * hand[1]
    return ans

if __name__ == "__main__":
    test = get_input(2023, 7, filename="test.txt")
    print("Test:")
    ##part_one(test)
    part_two(test)

    print("inp:")
    inp = get_input(2023, 7)
    #ans = part_one(inp)
    #submit(2023, 7, 1, ans)
    ans = part_two(inp)
    #submit(2023, 7, 2, ans)

