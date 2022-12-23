from advent import get_input
inp = get_input(2022, 17)[0]
inp = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

rocks = '''####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##'''.split('\n\n')
rocks = [i.splitlines() for i in rocks]
positions = set()

width = 7
rock_num = 0
move = 0
top = -1

#loops = 40
#for i in range(40):
    #fallen = False
    #y = top + 4
    #x = 2
    #rock = rocks[rock_num]
    #r_width = len(rock[0])
    #r_height = len(rock)
    #while not fallen:
        #dir = inp[move]
        #move = (move+1)%len(inp)
        #match dir:
            #case ">":
                #if x + r_width < width and not any((x+dx+1, y+dy) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
                    #x+=1
            #case "<":
                #if x > 0 and not any((x+dx-1, y+dy) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
                    #x-=1

        #if y-1>=0 and not any((x+dx, y+dy-1) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
            #y-=1
        #else:
            #fallen = True
            #for dy in range(r_height):
                #for dx in range(r_width):
                    #if rock[~dy][dx] == "#":
                        #positions.add((x+dx, y+dy))
    
    #ntop = max(positions, key=lambda x: x[1])[1]
    #delta =  ntop-top
    #top = ntop
    #rock_num = (rock_num+1)%5

#print(top)
iters= 1_000_000_000_000 # 1 trillion

#for i in reversed(range(top+1)):
    #print(f"{i:2d} |", end="")
    #for j in range(width):
        #if (j, i) in positions:
            #print("#", end="")
        #else:
            #print(".", end="")
    #print("|")
#print("   +", "-"*width, "+", sep="")


window = 20
#for i in range(40, top):
i=0
while True:
    fallen = False
    y = top + 4
    x = 2
    rock = rocks[rock_num]
    r_width = len(rock[0])
    r_height = len(rock)
    while not fallen:
        dir = inp[move]
        move = (move+1)%len(inp)
        match dir:
            case ">":
                if x + r_width < width and not any((x+dx+1, y+dy) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
                    x+=1
            case "<":
                if x > 0 and not any((x+dx-1, y+dy) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
                    x-=1

        if y-1>=0 and not any((x+dx, y+dy-1) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
            y-=1
        else:
            fallen = True
            for dy in range(r_height):
                for dx in range(r_width):
                    if rock[~dy][dx] == "#":
                        positions.add((x+dx, y+dy))
    
    ntop = max(positions, key=lambda x: x[1])[1]
    delta =  ntop-top
    top = ntop
    rock_num = (rock_num+1)%5
    iters-=1
    i+=1
    # check if prior 40 point window is the same as the start
    if i >window:
        pass
    break

    