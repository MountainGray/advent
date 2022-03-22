import sys

print(sys.path)
from aoc_utils import load_input


directions: list[str] = load_input(2016, 1)

#p1
orient = 0+1j
location = 0 + 0j
for direction in directions:
    if direction[0] == "L":
        orient *= 1j
    else:
        orient *= -1j

    location += int(direction[1:]) * orient
print("P1:", abs(location.imag) + abs(location.real))

#p2
orient = 0+1j
location = 0 + 0j
hist = []
cross = None
for direction in directions:
    if direction[0] == "L":
        orient *= 1j
    else:
        orient *= -1j
    for _ in range(int(direction[1:])):
        location += orient
        if location in hist:
            cross = abs(location.imag) + abs(location.real)
            break
        else:
            hist.append(location)
    if cross:
        break

print("P2:", cross)

