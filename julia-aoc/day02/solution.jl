inp = open(f->read(f, String),"2021/day02/input.txt","r")
commands = [split(x, " ") for x in split(inp, "\n")]

depth = 0
horizontal = 0
for x in commands
    direction, num = x[1], parse(Int,x[2])
    if direction == "forward"
        global horizontal += num
    elseif direction == "up"
        global depth -= num
    else
        global depth += num
    end
end
print(depth * horizontal)

depth = 0
horizontal = 0
aim = 0
for x in commands
    direction, num = x[1], parse(Int,x[2])
    if direction == "forward"
        global horizontal += num
        global depth += aim * num
    elseif direction == "up"
        global aim -= num
    else
        global aim += num
    end
end
print(depth * horizontal)


