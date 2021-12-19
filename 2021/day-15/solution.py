from collections import defaultdict
from heapq import heappush, heappop


def parse_input():
    return [[int(x) for x in line.strip()] for line in open("input.txt")]


def multiply_input(x):
    orig = parse_input()
    rs = len(orig)
    cs = len(orig[0])
    new = [[0 for _ in range(cs * x)] for _ in range(rs * x)]
    for r in range(len(orig)):
        for c in range(len(orig[0])):
            for i in range(x):
                for j in range(x):
                    new[rs * i + r][cs * j + c] = orig[r][c] + i + j
                    if new[rs * i + r][cs * j + c] > 9:
                        new[rs * i + r][cs * j + c] -= 9
    return new


def neighbors(r, c, cave):
    return [
        (r + dr, c + dc, cave[r + dr][c + dc])
        for dr in range(-1, 2)
        for dc in range(-1, 2)
        if 0 <= r + dr < len(cave)
        and 0 <= c + dc < len(cave[0])
        and (dr != 0 or dc != 0)
        and (dr == 0 or dc == 0)
    ]


def to_graph(cave):
    start, end = (0, 0, cave[0][0]), (len(cave) - 1, len(cave[0]) - 1, cave[-1][-1])
    graph = defaultdict(list)
    for r in range(len(cave)):
        for c in range(len(cave[0])):
            for n in neighbors(r, c, cave):
                graph[(r, c, cave[r][c])].append(n)
    return graph, start, end


def shortest_path(graph, start, end):
    queue = [(0, start)]
    visited = set()
    while queue:
        distance, node = heappop(queue)
        if node == end:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                heappush(queue, (distance + neighbor[2], neighbor))
    return None


def solve_part_one():
    cave, start, end = to_graph(parse_input())
    return shortest_path(cave, start, end)


def solve_part_two():
    cave, start, end = to_graph(multiply_input(5))
    return shortest_path(cave, start, end)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
