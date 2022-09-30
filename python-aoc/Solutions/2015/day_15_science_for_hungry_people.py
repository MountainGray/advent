from advent import get_input, solution_timer

@solution_timer(2015, 15, 1)
def part_one(input_data: list[str]):
    input = input_parse(input_data)
    ingredient_list = list(input.values())
    properties_list = list(ingredient_list[0].keys())

    max_score = 0
    for i in range(101):
        for j in range(101-i):
            for k in range(101-i-j):
                l = 100-i-j-k
                total = 1
                for property in properties_list[:-1]: # skip calories
                    buf_total = 0
                    for ingredient, ammount in zip(ingredient_list, [i, j, k, l]):
                        buf_total +=  ammount * ingredient[property]
                    total *= max(0, buf_total)
                    #print(total)
                max_score = max(max_score, total)

    return max_score

@solution_timer(2015, 15, 2)
def part_two(input_data: list[str]):
    input = input_parse(input_data)
    ingredient_list = list(input.values())
    properties_list = list(ingredient_list[0].keys())

    max_score = 0
    for i in range(101):
        for j in range(101-i):
            for k in range(101-i-j):
                l = 100-i-j-k
                total = 1
                calories = 0
                for ingredient, ammount in zip(ingredient_list, [i, j, k, l]):
                    calories += ammount * ingredient["calories"]
                
                if calories != 500: # break for cal limit
                    continue

                for property in properties_list[:-1]: # skip calories
                    calories = 0
                    buf_total = 0
                    for ingredient, ammount in zip(ingredient_list, [i, j, k, l]):
                        buf_total +=  ammount * ingredient[property]
                    total *= max(0, buf_total)
                max_score = max(max_score, total)

    return max_score

    


def input_parse(inp: list[str]) -> dict[str, dict[str, int]]:
    ingredients: dict[str, dict[str, int]]= {}
    for line in inp:
        ingredient, properties = line.split(": ")
        properties = properties.split(", ")
        properties = [prop.split(" ") for prop in properties]
        ingredients[ingredient] = {prop[0]: int(prop[1]) for prop in properties}

    return ingredients

if __name__ == "__main__":
    inp = get_input(2015, 15)
    part_one(inp)
    part_two(inp)
