inp = open("2021/day02/input.txt", "r").read().split("\n")
depth = 0
horizontal = 0

for x in inp:
    command, num = x.split(" ")
    if command == "forward":
        horizontal += int(num)
    if command == "up":
        depth -= int(num)
    if command == "down":
        depth += int(num)

print("P1", horizontal * depth)

# p1
aim = 0
depth = 0
horizontal = 0

for x in inp:
    command, num = x.split(" ")
    if command == "forward":
        horizontal += int(num)
        depth += aim * int(num)
    if command == "up":
        aim -= int(num)
    if command == "down":
        aim += int(num)

print("P2", horizontal * depth)
