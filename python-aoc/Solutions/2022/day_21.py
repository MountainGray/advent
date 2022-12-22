from advent import get_input, solution_timer
import sympy as sym

vals = {}

@solution_timer(2022, 21, 1)
def part_one(inp):
    for i in inp:
        a, b = i.split(": ")
        vals[a] = b

    def get_val(a):
        b = vals[a]
        if b.isnumeric():
            return b
        else:
            x, op, y = b.split()
            return eval(f"{get_val(x)} {op} {get_val(y)}")
    return int(get_val("root"))

@solution_timer(2022, 21, 2)
def part_two():
    vals["humn"]="x"
    a, _, b = vals["root"].split()
    def get_eqn(a):
        b = vals[a]
        if b.isnumeric():
            return b
        elif b=="x":
            return "x"
        else:
            x, op, y = b.split()
            return f"({get_eqn(x)}) {op} ({get_eqn(y)})"

    eq1 = get_eqn(a)
    eq2 = get_eqn(b)

    x = sym.symbols("x")
    eqn = sym.Eq((eval(eq1)) , (eval(eq2)))
    result = sym.solve(eqn, x)
    return int(result[0])

if __name__ == "__main__":
    input = get_input(2022, 21)
    part_one(input)
    part_two()
