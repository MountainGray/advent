from advent import get_input, solution_timer
import re

# TODO

@solution_timer(2015, 11, 1)
def part_one(input_data: list[str]):
    password = input_data[0]
    while True:
        password = increment_password(password)
        if valid_password(password):
            return password


@solution_timer(2015, 11, 2)
def part_two(password: str):
    while True:
        password = increment_password(password)
        if valid_password(password):
            return password


def increment_password(password: str) -> str:
    seq = [ord(ch) for ch in password]
    for i in range(len(password) - 1, -1, -1):
        if seq[i] == 122:
            seq[i] = 97
        else:
            if seq[i] == 104:  # skip "i"
                seq[i] = 106
            elif seq[i] == 107:  # skip "l"
                seq[i] = 109
            elif seq[i] == 110:  # skip "o"
                seq[i] = 112
            else:
                seq[i] += 1
            break
    return "".join(map(chr, seq))


def valid_password(password: str) -> bool:

    incr_seq = False
    seq = [ord(ch) for ch in password]
    for i in range(len(password) - 2):
        if seq[i] == seq[i + 1] - 1 and seq[i + 1] == seq[i + 2] - 1:
            incr_seq = True
            break
    if not incr_seq:
        return False

    pairs = 0
    for ch in set(password):
        regex = re.compile(f"{ch}{ch}")
        if regex.search(password):
            pairs += 1
    if pairs < 2:
        return False
    return True


if __name__ == "__main__":
    inp = get_input(2015, 11)
    p1_password = part_one(inp)
    part_two(p1_password)
