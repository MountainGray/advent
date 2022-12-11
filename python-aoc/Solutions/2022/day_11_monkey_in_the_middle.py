from advent import get_input, solution_timer
from functools import reduce

class monkey:
    def __init__(self, start_items, operation, num,  test, m1, m2, m) -> None:
        self.items = start_items
        self.operation = operation
        self.num = num
        self.test = test
        self.m1 = m1
        self.m2 = m2
        self.m = m
        self.inspected = 0
        self.crt = -1

    def turn(self):
        while len(self.items) > 0:
            self.inspected += 1
            item = self.items.pop(0)
            if self.operation == "*":
                if self.num == "old": worry = item * item
                else: worry = item * int(self.num)
            else:
                if self.num == "old": worry = item + item
                else: worry = item + int(self.num)
            if self.crt != -1: worry = worry % self.crt
            else: worry //=3
            if worry %self.test == 0: self.m[self.m1].items.append(worry)
            else: self.m[self.m2].items.append(worry)
    def crt_val(self, crt):
        self.crt = crt

def parse_input(inp, md):
    for mon in inp:
        _, items, operation, test, m1, m2 = mon.splitlines()
        items = [int(i) for i in items.split(": ")[1].split(", ")]
        operation = operation.split(" = ")[1].split(" ")[1]
        od = operation.split(" = ")[1].split(" ")[2]
        test = int(test.split(" ")[-1])
        m1= int(m1.split(" ")[-1])
        m2= int(m2.split(" ")[-1])
        md.append(monkey(items, operation, od,test, m1, m2, md))


@solution_timer(2022, 11, 1)
def part_one(inp):
    parse_input(inp, md:=[])
    for _ in range(20):
        for m in md:
            m.turn()
    
    return reduce(lambda a, b: a*b,sorted([m.inspected for m in md])[-2:])

@solution_timer(2022, 11, 2)
def part_two(inp):
    parse_input(inp, md:=[])
    crt = reduce(lambda a, b: a*b,[m.test for m in md])
    for m in md: m.crt_val(crt)
    for _ in range(10000):
        for m in md:
            m.turn()
    
    return reduce(lambda a, b: a*b,sorted([m.inspected for m in md])[-2:])

if __name__ == "__main__":
    input = get_input(2022, 11, split_char="\n\n")
    part_one(input)
    part_two(input)
