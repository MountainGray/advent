from advent import get_input, solution_timer
import hashlib

# Possible improvements?


def md5_imported(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


@solution_timer(2015, 4, 1)
def part_one(input_data: list[str]):
    secret_key = input_data[0]
    x = 0
    while True:
        hsh = md5_imported(secret_key + str(x))
        if hsh[:5] == "00000":
            return x
        x += 1


@solution_timer(2015, 4, 2)
def part_two(input_data: list[str]):
    secret_key = input_data[0]

    x = 0
    while True:
        hsh = md5_imported(secret_key + str(x))
        if hsh[:6] == "000000":
            return x
        x += 1


if __name__ == "__main__":
    data = get_input(2015, 4)
    part_one(data)
    part_two(data)
