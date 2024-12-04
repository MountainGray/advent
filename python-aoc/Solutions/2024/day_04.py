from advent import get_input, solution_timer
from advent.helpers import rotate_grid_cw

@solution_timer(2024, 4, 1)
def part_one(inp: list[str]):
    ans = 0
    for _ in range(2):
        inp = rotate_grid_cw(inp)
        inp = ["".join(i) for i in inp]
        for i in range(len(inp)-3):
            x = "".join(inp[i:i+4])
            if x == "XMAS" or x == "SAMX":
                ans += 1
        for i in range(len(inp) - 3):
            for j in range(len(inp) - 3):
                diag = "".join([inp[j+x][i + x] for x in range(4)])
                if diag == "XMAS":
                    ans += 1
                if diag == "SAMX":
                    ans += 1
    return ans


@solution_timer(2024, 4, 1)
def part_two(inp: list[str]):
    ans = 0
    for i in range(len(inp) - 2):
        for j in range(len(inp) - 2):
            diag1 = "".join([inp[j+x][i + x] for x in range(3)])
            diag2 = "".join([inp[j+2-x][i + x] for x in range(3)])
            if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                ans += 1
    return ans

if __name__ == "__main__":
    inp = get_input(2024, 4, split_char="\n")
    part_one(inp)
    part_two(inp)
