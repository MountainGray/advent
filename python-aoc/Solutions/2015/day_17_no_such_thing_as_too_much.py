from advent import get_input, solution_timer
from functools import lru_cache
global counter
counter = 0
@solution_timer(2015, 17, 1)
def part_one(input_data: list[str]):
    cubesa = tuple(map(int, input_data))

    @lru_cache(None)
    def recur(size: int, cubes: tuple[int]):
        if size == 0:
            return 1
        elif size < 0:
            return 0
        elif len(cubes)==0:
            return 0
        else:
            sa = 0
            sc = list(cubes)
            for i in range(len(cubes)):
                a = sc.copy()[i+1:]
                sa += recur(size - cubes[i], tuple(a))
            return sa
    return recur(150, cubesa)
    

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
            sc = list(cubes)
            for i in range(len(cubes)):
                a = sc.copy()[i+1:]
                min_cup_fills = recur(size - cubes[i], tuple(a), cont_used+1, min_cup_fills)
            return min_cup_fills
        else:
            return min_cup_fills
    return recur(150, cubesa, 0, (len(cubesa),0))

if __name__ == "__main__":
    inp = get_input(2015, 17)
    part_one(inp)
    part_two(inp)