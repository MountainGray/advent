from advent import get_input, solution_timer
from functools import lru_cache

@solution_timer(2015, 17, 1)
def part_one(input_data: list[str]):
    cubes = tuple(map(int, input_data))

    @lru_cache(None)
    def recur(size: int, cubes: tuple[int]):
        if size == 0:
            return 1
        elif size < 0:
            return 0
        elif len(cubes)==0:
            return 0
        else:
            filled = 0
            cubes_list = list(cubes)
            for i in range(len(cubes)):
                cubes_slice = cubes_list[i+1:]
                filled += recur(size - cubes[i], tuple(cubes_slice))
            return filled
    return recur(150, cubes)
    

@solution_timer(2015, 17, 2)
def part_two(input_data: list[str]):
    cubesa = tuple(map(int, input_data))
    
    @lru_cache(None)
    def recur(size: int, cubes: tuple[int], cont_used: int ,min_cup_fills: tuple[int, int]):
        if size == 0:
            if cont_used == min_cup_fills[0]:
                return (cont_used, min_cup_fills[1] + 1)
            elif cont_used < min_cup_fills[0]:
                return (cont_used, 1)
            else:
                return min_cup_fills
        elif len(cubes)==0:
            return min_cup_fills
        elif size > 0:
            cube_list = list(cubes)
            for i in range(len(cubes)):
                cube_slice = cube_list[i+1:]
                min_cup_fills = recur(size - cubes[i], tuple(cube_slice), cont_used+1, min_cup_fills)
            return min_cup_fills
        else:
            return min_cup_fills
    return recur(150, cubesa, 0, (len(cubesa),0))

if __name__ == "__main__":
    inp = get_input(2015, 17)
    part_one(inp)
    part_two(inp)