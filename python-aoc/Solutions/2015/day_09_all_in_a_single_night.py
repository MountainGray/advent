from advent import get_input, solution_timer


@solution_timer(2015, 9, 1)
def part_one(input_data: list[str]):
    nodes = parse_input(input_data)
    distance = solution(nodes,  "0")
    return distance


START = "Faerun"
END = "straylight"


def solution(nodes: dict[str, list[tuple[str, int]]], start: str) -> int:

    def recurse(node: str, distance: int, visited: list[str]) -> int:
        min_distance = 1000
        if node == END:
            return distance
        for end, dist in nodes[node]:
            if end not in visited:
                dist = recurse(end, distance + dist, visited+[end])
                if dist is not None:
                    min_distance = min(min_distance, dist)
        return min_distance

    distance = recurse(START, 0, [START])

    return distance


def parse_input(input_data: list[str]) -> dict[str, list[tuple[str, int]]]:
    nodes = {}
    for line in input_data:
        start, _, end, _, distance = line.split()
        if start not in nodes:
            nodes[start] = []
        nodes[start].append((end, int(distance)))
    
    print(nodes)

    return nodes


if __name__ == "__main__":
    inp = get_input(2015, 9)
    part_one(inp)
