from advent import get_input, solution_timer

def parse_input(inp):
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
    moves.append(int(v)) # this freaking line cost me 6 hours
    return positions, moves


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
ori_score = {
    1 + 0j: 0,
    0 + 1j: 1,
    -1 + 0j: 2,
    0 - 1j: 3
}

@solution_timer(2022, 22, 1)
def part_one(inp):
    positions, moves = parse_input(inp)

    position = 50 + 0j
    orientation = 1 + 0j
    
    for i in moves:
        if isinstance(i, int):
            for _ in range(i):
                if position + orientation in positions:
                    if positions[position + orientation][0] == "#":
                        break
                    else:
                        position += orientation
                else:
                    # check loop around
                    if orientation == 1 + 0j:
                        val = min(filter(lambda x: x.imag==position.imag, positions.keys()), key=lambda x: x.real)
                        if positions[val][0] == "#":
                            break
                        else:
                            position = val
                    elif orientation == -1 + 0j:
                        val = max(filter(lambda x: x.imag==position.imag, positions.keys()), key=lambda x: x.real)
                        if positions[val][0] == "#":
                            break
                        else:
                            position = val
                    elif orientation == 0 + 1j:
                        val = min(filter(lambda x: x.real==position.real, positions.keys()), key=lambda x: x.imag)
                        if positions[val][0] == "#":
                            break
                        else:
                            position = val
                    elif orientation == 0 - 1j:
                        val = max(filter(lambda x: x.real==position.real, positions.keys()), key=lambda x: x.imag)
                        if positions[val][0] == "#":
                            break
                        else:
                            position = val
        else:
            if i == "R":
                orientation *= 1j
            elif i == "L":
                orientation *= -1j

    return int((position.imag+1)* 1000 + 4*(position.real+1) + ori_score[orientation])

@solution_timer(2022, 22, 2)
def part_two(inp):
    positions, moves = parse_input(inp)
    position = 50 + 0j
    orientation = 1 + 0j

    for i in moves:
        if isinstance(i, int):
            # walk along path and stop at #
            for j in range(i):
                _, sector = positions[position]
                if position + orientation in positions:
                    if positions[position + orientation][0] == "#":
                        break
                    else:
                        position += orientation
                else:
                    p_funk, ori = translations[sector][orientation]
                    if positions[p_funk(position)][0] == "#":
                        break
                    else:
                        position = p_funk(position)
                        orientation = ori
        else:
            if i == "R":
                orientation *= 1j
            elif i == "L":
                orientation *= -1j



    return int((position.imag+1)* 1000 + 4*(position.real+1) + ori_score[orientation])



if __name__ == "__main__":
    input = get_input(2022, 22, split_char="\n\n")
    part_one(input)
    part_two(input)

