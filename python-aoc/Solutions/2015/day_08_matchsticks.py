from advent import get_input, solution_timer


@solution_timer(2015, 8, 1)
def part_one(input_data: list[str]):
    char_input = 0
    char_memory = 0

    for line in input_data:
        char_input += len(line)
        line = line[1:-1]
        ptr = 0
        while ptr < len(line):
            if line[ptr] == "\\":
                if line[ptr+1] == "x":
                    char_memory += 1
                    ptr += 4
                else:
                    char_memory += 1
                    ptr += 2
            else:
                char_memory += 1
                ptr += 1

    return char_input - char_memory


@solution_timer(2015, 8, 2)
def part_two(input_data: list[str]):
    char_input = 0
    char_expanded = 0

    for line in input_data:
        char_input += len(line)
        char_expanded += \
            len(line.replace("\\", "\\\\")
                    .replace("\"", "\\\"")) + 2

    return char_expanded - char_input


if __name__ == "__main__":
    inp = get_input(2015, 8)
    part_one(inp)
    part_two(inp)
