from advent import get_input, solution_timer


@solution_timer(2015, 10, 1)
def part_one(input_data: list[str]):
    sequence = input_data[0]
    for _ in range(40):
        sequence = look_and_say(sequence)

    return len(sequence)

@solution_timer(2015, 10, 2)
def part_two(input_data: list[str]):
    sequence = input_data[0]
    for _ in range(50):
        sequence = look_and_say(sequence)

    return len(sequence)


def look_and_say(sequence: str) -> str:
    count = 0
    sum_char = sequence[0]
    ret_str = ""
    for ch in sequence:
        if ch == sum_char:
            count += 1
        else:
            ret_str += str(count) + sum_char
            sum_char = ch
            count = 1

    return ret_str + str(count) + sum_char


if __name__ == "__main__":
    inp = get_input(2015, 10)
    part_one(inp)
    part_two(inp)
