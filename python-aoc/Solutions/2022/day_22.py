from advent import get_input

inp = get_input(2022, 22, split_char="\n\n")
m, dr = inp

m= m.splitlines()


positions = {}
width = 50

for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] in ["#", "."]:
            positions[complex(j,i)] = [m[i][j], 3*(i//width) + j//width]



moves = []
v=""
for i in dr:
    if not i.isnumeric():
        moves.append(int(v))
        v=""
        moves.append(i)
    else:
        v+=i
moves.append(int(v))

def print_map():
    for i in range(len(m)):
        for j in range(len(m[i])):
            if complex(j,i) in positions:
                print(positions[complex(j,i)][0], end="")
            else:
                print(" ", end="")
        print()

    for i in range(len(m)):
        for j in range(len(m[i])):
            if complex(j,i) in positions:
                print(positions[complex(j,i)][1], end="")
            else:
                print(" ", end="")
        print()
print(moves)

translations = {
    1: {
        # go up to 9 on the right
        0-1j: (lambda x: 0 + (150 + (x.real%50))*1j, 1+0j),
        # go left to 6 on the left upside down
        -1+0j: (lambda x: 0 + (100 + (49-x.imag))*1j, 1+0j),
        },
    2: {
        # go up to 9 on the bottom
        0-1j: (lambda x: (x.real%50) + 199j, 0-1j),
        # go right to 7 upside down
        1+0j: (lambda x: (99)+(100+49-x.imag)*1j, -1+0j),
        # go down to 4 on the right
        0+1j: (lambda x: 99+(50+(x.real%50))*1j, -1+0j)
        },
    4: {
        # going left to top of 6
        -1+0j: (lambda x: (x.imag%50) + 100j, 0+1j),
        # going right to bottom of 2
        1+0j: (lambda x: (100 + (x.imag%50)) + 49j, 0-1j),
        },
    6: {
        # go up to left of 4
        0-1j: (lambda x: 50 + (50+ x.real)*1j, 1+0j),
        # go left to 1 upside down
        -1+0j: (lambda x: 50 + (49 - (x.imag%50))*1j, 1+0j),

    },
    7: {
        # go right to 2 upsidedown
        1+0j: (lambda x: 149 + (49- (x.imag%50))*1j, -1+0j),
        # go down to 9 from the right
        0+1j: (lambda x: 49 + (150 + (x.real%50))*1j, -1+0j),
    },
    9: {
        # go right to 7 from the bottom
        1+0j: (lambda x: (50+x.imag%50)+ 149j, 0-1j),
        # go down to 2 from the top
        0+1j: (lambda x: (100 + x.real) + 0j, 0+1j),
        # go left to one from the top
        -1+0j: (lambda x: (50+ (x.imag%50)) + 0j, 0+1j),
    }
    }

start = 50+0j
orientation = 1 + 0j

for i in moves:
    if isinstance(i, int):
        # walk along path and stop at #
        for j in range(i):
            _, sector = positions[start]
            if start + orientation in positions:
                if positions[start + orientation][0] == "#":
                    break
                else:
                    if orientation == 1 + 0j:
                        positions[start][0] = ">"
                    elif orientation == -1 + 0j:
                        positions[start][0] = "<"
                    elif orientation == 0 + 1j:
                        positions[start][0] = "v"
                    elif orientation == 0 - 1j:
                        positions[start][0] = "^"
                    start += orientation
            else:
                p_funk, ori = translations[sector][orientation]
                if positions[p_funk(start)][0] == "#":
                    break
                else:
                    if orientation == 1 + 0j:
                        positions[start][0] = ">"
                    elif orientation == -1 + 0j:
                        positions[start][0] = "<"
                    elif orientation == 0 + 1j:
                        positions[start][0] = "v"
                    elif orientation == 0 - 1j:
                        positions[start][0] = "^"
                    start = p_funk(start)
                    orientation = ori
                    #print_map()
    else:
        if i == "R":
            orientation *= 1j
        elif i == "L":
            orientation *= -1j

extra = 0
if orientation == 1 + 0j:
    extra = 0
elif orientation == -1 + 0j:
    extra = 2
elif orientation == 0 + 1j:
    extra = 1
elif orientation == 0 - 1j:
    extra = 3
print(start)


x = int((start.imag+1)* 1000 + 4*(start.real+1) + extra)
print(x)


#for i in moves:
    #if isinstance(i, int):
        ## walk along path and stop at #
        #for j in range(i):
            #if start + orientation in positions:
                #if positions[start + orientation] == "#":
                    #break
                #else:
                    #start += orientation
            #else:
                ## check loop around
                #if orientation == 1 + 0j:
                    #val = min(filter(lambda x: x.imag==start.imag, positions.keys()), key=lambda x: x.real)
                    #if positions[val] == "#":
                        #break
                    #else:
                        #start = val
                #elif orientation == -1 + 0j:
                    #val = max(filter(lambda x: x.imag==start.imag, positions.keys()), key=lambda x: x.real)
                    #if positions[val] == "#":
                        #break
                    #else:
                        #start = val
                #elif orientation == 0 + 1j:
                    #val = min(filter(lambda x: x.real==start.real, positions.keys()), key=lambda x: x.imag)
                    #if positions[val] == "#":
                        #break
                    #else:
                        #start = val
                #elif orientation == 0 - 1j:
                    #val = max(filter(lambda x: x.real==start.real, positions.keys()), key=lambda x: x.imag)
                    #if positions[val] == "#":
                        #break
                    #else:
                        #start = val
    #else:
        #if i == "R":
            #orientation *= 1j
        #elif i == "L":
            #orientation *= -1j