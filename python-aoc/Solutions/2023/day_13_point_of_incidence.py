from advent import get_input, solution_timer
from advent.helpers import transpose_grid


def find_mirror(pat):
    for i in range(1, len(pat)):
        first = pat[:i]
        second = pat[i:]
        pars = zip(list(reversed(first)), second)
        if all([x == y for x, y in pars]):
            return i
    return False


def find_both(pat):
    if ret := find_mirror(pat):
        return 100 * ret
    else:
        return find_mirror(transpose_grid(pat))


@solution_timer(2023, 13, 1)
def part_one(inp):
    return sum([find_both(pat.split("\n")) for pat in inp])


def find_mirrors(pat):
    s = []
    for i in range(1, len(pat)):
        first = pat[:i]
        second = pat[i:]
        pars = zip(list(reversed(first)), second)
        if all([x == y for x, y in pars]):
            s += [i]
    return s


def find_all_mirrors(pat):
    return [x * 100 for x in find_mirrors(pat)] + find_mirrors(transpose_grid(pat))


def find_smudge(pat) -> int:
    npat = [[x for x in line] for line in pat.split("\n")]
    old = find_all_mirrors(npat)[0]
    for y in range(len(npat)):
        for x in range(len(npat[0])):
            tpat = [[x for x in line] for line in npat]
            if npat[y][x] == "#":
                tpat[y][x] = "."
            else:
                tpat[y][x] = "#"
            new = find_all_mirrors(tpat)
            if old in new:
                new.remove(old)
            if len(new) > 0:
                return new[0]


@solution_timer(2023, 13, 2)
def part_two(inp):
    sans = 0
    for pat in inp:
        sans += find_smudge(pat)
    return sans


if __name__ == "__main__":
    inp = get_input(2023, 13, split_char="\n\n")
    part_one(inp)
    part_two(inp)
