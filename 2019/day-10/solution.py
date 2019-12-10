from math import gcd, inf
from collections import defaultdict


def parse_input():
    return [(x, y) for y, line in enumerate(open('input.txt').readlines())
            for x, c in enumerate(line) if c == '#']


def get_dir(a, b):
    ax, ay = a
    bx, by = b

    dx = bx - ax
    dy = by - ay
    g = gcd(dx, dy)

    return (dx / g, dy / g)


def find_best_location(coords):
    counts = {}
    for c1 in coords:
        dirs = set()
        for c2 in coords:
            if c1 != c2:
                dir = get_dir(c1, c2)
                dirs.add(dir)
        counts[c1] = len(dirs)
    return max(counts.items(), key=lambda x: x[1])


def dist(a, b):
    ax, ay = a
    bx, by = b
    return abs(ay - ax) + abs(by - ay)


def group_per_direction(laser, coords):
    grouped = defaultdict(list)
    for c in coords:
        dir = get_dir(laser, c)
        grouped[dir].append(c)

    for cs in grouped.values():
        cs.sort(key=lambda c: dist(laser, c))

    return grouped


def solve_part_one():
    coords = parse_input()
    _, in_sight = find_best_location(coords)
    return in_sight


def sort_key(c):
    x, y = c
    if x == 0:
        s = -inf
        d = y > 0
    else:
        s = y / x
        d = x < 0
    return (d, s)


def solve_part_two():
    coords = parse_input()
    laser, _ = find_best_location(coords)
    coords.remove(laser)

    grouped = group_per_direction(laser, coords)

    directions = list(grouped.keys())
    directions.sort(key=sort_key)

    n = 0
    while True:
        for dir in directions:
            if len(grouped[dir]):
                n += 1
                shot = grouped[dir].pop(0)
                if n == 200:
                    return shot[0] * 100 + shot[1]


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
