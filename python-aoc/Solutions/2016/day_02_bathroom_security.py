from advent import get_input
inp = get_input(2016, 2)

# p1
code = []
cord = 0 + 0j
for direction in inp:
    for d in direction:
        if d == "U" and cord.imag < 1:
            cord += 1j
        elif d == "R" and cord.real < 1:
            cord += 1
        elif d == "L" and cord.real > -1:
            cord -= 1
        elif d == "D" and cord.imag > -1:
            cord -= 1j

    code.append(int(5 + (-3) * cord.imag + cord.real))

print("P1: ", code)

# p2
pad = '''  1  
 234 
56789
 ABC 
  D  '''.splitlines()

# index [y][x]
code = []
x, y = 2, 0
for direction in inp:
    for d in direction:
        if d == "U" and y > 0 and pad[y-1][x] != " ":
            y -= 1
        if d == "D" and y < 4 and pad[y+1][x] != " ":
            y += 1
        if d == "L" and x > 0 and pad[y][x-1] != " ":
            x -= 1
        if d == "R" and x < 4 and pad[y][x+1] != " ":
            x += 1
    code.append(pad[y][x])

print("P2: ", "".join(code))
