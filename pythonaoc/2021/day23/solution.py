inp = open('2021/day23/input.txt').read().split('\n')

p1input = (("D","C"),("D","C"),("A","B"),("A","B"))

depth = len(p1input[0])
rooms = (2,4,6,8)
position = ("A","B","C","D")
halls = (0,1,3,5,7,9,10)
hallstate = ((None,)*11)
cost = {
    "A":1,
    "B":10,
    "C":100,
    "D":1000,
}

def recurse(rooms, halls):
    for i, room in enumerate(rooms):
        for j, amph in enumerate(rooms):
            if amph == None: continue
            elif amph == position[i] and ((None,)*j+(amph,)*(depth-i))==room:break
            else:#move to hall
                



