fn = open('Day22/input.txt')
decks=fn.read().split('\n\n')
players=[]
for deck in decks:
    hand=[int(i) for i in deck.splitlines()[1:]]
    players.append(hand)
p2=copy.deepcopy(players)
while True:
    card1=players[0].pop(0)
    card2=players[1].pop(0)
    if card1 > card2:
        players[0].append(card1)
        players[0].append(card2)
    elif card2>card1:
        players[1].append(card2)
        players[1].append(card1)
    if len(players[0])==0 or len(players[1])==0:
        break
ans=0
for i, val in enumerate(players[0]):
    ans+= (len(players[0])-i)*val
print('Part 1',ans)
finalhand=[]
def recursComb(hands,top=False):
    
    games=[]
    winner=None
    while True:
        if hands[0] in games:
            winner=0
            break
        games.append(hands[0].copy())
        games.append(hands[1].copy())
        card1=hands[0].pop(0)
        card2=hands[1].pop(0)
        if card1<=len(hands[0]) and card2<=len(hands[1]):
            ret=recursComb([hands[0][:card1].copy(),hands[1][:card2].copy()])
            if ret==0:
                hands[0].append(card1)
                hands[0].append(card2)
            else:
                hands[1].append(card2)
                hands[1].append(card1)
        elif card1 > card2:
            hands[0].append(card1)
            hands[0].append(card2)
        elif card2>card1:
            hands[1].append(card2)
            hands[1].append(card1)

        if len(hands[0])==0 or len(hands[1])==0:
            break
    if top==True:
        if len(hands[0])==0:
            return hands[1]
        else:
            return hands[0]
    if len(hands[0])==0:
        return 1
    else:
        return 0
finalhand=recursComb(p2,True)  
ans3=0
for i, val in enumerate(finalhand):
    ans3+= (len(finalhand)-i)*val
print("Part 2",ans3) 