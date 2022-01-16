inp = open("2016/day02/input.txt").read().split("\n")

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
pad = [
    [1],
    [2, 3, 4],
    [5, 6, 7, 8, 9],
    ["A", "B", "C"],
    ["D"],
]# index [y][x]
code = []
cord = 0 + 2j #x, y
for direction in inp:
    for d in direction:
        if d == "U" and cord.imag > 0 and cord.real:
            cord -= 1j
        elif d == "R" and cord.real < 1:
            cord += 1
        elif d == "L" and cord.real > -1:
            cord -= 1
        elif d == "D" and cord.imag > -1:
            cord -= 1j

def valid(point):
    if(point.)