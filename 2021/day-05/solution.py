import re
from collections import defaultdict

regex = re.compile("(\d+),(\d+) -> (\d+),(\d+)")


def parse_input():
    result = []
    for line in open("input.txt"):
        x1, y1, x2, y2 = regex.match(line).groups()
        result.append((int(x1), int(y1), int(x2), int(y2)))
    return result


def covered_points(line):
    x1, y1, x2, y2 = line
    points = set()
    if x1 == x2:
        step = 1 if y1 < y2 else -1
        for y in range(y1, y2 + step, step):
            points.add((x1, y))
    elif y1 == y2:
        step = 1 if x1 < x2 else -1
        for x in range(x1, x2 + step, step):
            points.add((x, y1))
    else:
        dx = (x2 - x1) / abs(x2 - x1)
        dy = (y2 - y1) / abs(y2 - y1)
        i = 0
        while True:
            points.add((x1 + i * dx, y1 + i * dy))
            if x1 + i * dx == x2:
                break
            i += 1

    return points


def solve_part_one():
    lines = list(
        filter(lambda line: line[0] == line[2] or line[1] == line[3], parse_input())
    )
    counts = defaultdict(int)
    for line in lines:
        for point in covered_points(line):
            counts[point] += 1
    return sum(1 for c in counts.values() if c > 1)


def solve_part_two():
    lines = parse_input()
    counts = defaultdict(int)
    for line in lines:
        for point in covered_points(line):
            counts[point] += 1
    return sum(1 for c in counts.values() if c > 1)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
