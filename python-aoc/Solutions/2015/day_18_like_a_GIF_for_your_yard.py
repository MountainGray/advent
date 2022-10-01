# hey, is this the game of life?

from advent import get_input_grid, solution_timer

@solution_timer(2015, 18, 1)
def part_one(input_data: list[list[int]]):
    def step(input_grid):
        output_grid = [[0 for _ in range(100)] for _ in range(100)]
        for y in range(100):
            for x in range(100):
                lit_n = 0
                for i in range(-1, 2):
                    for j in range(-1,2):
                        m = y+j
                        n = x+i
                        if (
                            (i !=0 or j !=0) and
                            (n >=0 and n< 100) and
                            (m >=0 and m < 100)
                            ):
                            lit_n += input_grid[m][n]
                if input_grid[y][x] == 1:
                    if lit_n == 2 or lit_n == 3:
                        output_grid[y][x] = 1
                else:
                    if lit_n == 3:
                        output_grid[y][x] = 1
        
        return output_grid

    for _ in range(100):
        input_data = step(input_data)
    
    return sum(map(sum, input_data))
    
@solution_timer(2015, 18, 2)
def part_two(input_data: list[list[int]]):
    def step(input_grid):
        output_grid = [[0 for _ in range(100)] for _ in range(100)]
        for y in range(100):
            for x in range(100):
                lit_n = 0
                for i in range(-1, 2):
                    for j in range(-1,2):
                        m = y+j
                        n = x+i
                        if (
                            (i !=0 or j !=0) and
                            (n >=0 and n< 100) and
                            (m >=0 and m < 100)
                            ):
                            lit_n += input_grid[m][n]
                if input_grid[y][x] == 1:
                    if lit_n == 2 or lit_n == 3:
                        output_grid[y][x] = 1
                else:
                    if lit_n == 3:
                        output_grid[y][x] = 1
        output_grid[0][0] = 1
        output_grid[0][99] = 1
        output_grid[99][0] = 1
        output_grid[99][99] = 1
        
        return output_grid
    input_data[0][0] = 1
    input_data[0][99] = 1
    input_data[99][0] = 1
    input_data[99][99] = 1

    for _ in range(100):
        input_data = step(input_data)
    
    return sum(map(sum, input_data))

def inp_cnv(char: str):
    if char == "#":
        return 1
    else:
        return 0

if __name__ == "__main__":
    inp = get_input_grid(2015, 18, inp_cnv)
    part_one(inp)
    part_two(inp)