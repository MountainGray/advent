from advent import get_input, solution_timer

SUE_SPEC = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

@solution_timer(2015, 16, 1)
def part_one(input_data: list[str]):
    sue_dict = input_parse(input_data)
    for sue, items in sue_dict.items():
        for item, value in items.items():
            if value != SUE_SPEC[item]:
                break
        else:
            return sue

@solution_timer(2015, 16, 2)
def part_two(input_data: list[str]):
    sue_dict = input_parse(input_data)
    for sue, items in sue_dict.items():
        for item, value in items.items():
            if item in ["cats", "trees"]:
                if value <= SUE_SPEC[item]:
                    break
            elif item in ["pomeranians", "goldfish"]:
                if value >= SUE_SPEC[item]:
                    break
            else:
                if value != SUE_SPEC[item]:
                    break
        else:
            return sue

def input_parse(input_data: list[str]):
    sue_dict = {}
    for line in input_data:
        split_point = line.find(': ')
        sue = int(line[:split_point].split(' ')[1])
        items = list(map(lambda x: x.split(": "), line[split_point+2:].split(', ')))
        sue_dict[sue] = {item[0]: int(item[1]) for item in items}

    return sue_dict


if __name__ == "__main__":
    inp = get_input(2015, 16)
    part_one(inp)
    part_two(inp)
