from collections import Counter, defaultdict
from operator import itemgetter

MIN_GRID = 0
MAX_GRID = 500

TOTAL_DIST_LIMIT = 10000

def parse_input():
    return [tuple(map(int, line.strip().split(', '))) for line in open('input.txt')]

def dist(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)


def solve_part_one():
    coords = parse_input()
    grid = dict()

    for x in range(MIN_GRID, MAX_GRID+1):
        for y in range(MIN_GRID, MAX_GRID+1):
            ds = defaultdict(list)

            for idx, (a, b) in enumerate(coords):
                ds[dist(x, y, a, b)].append(idx)

            d, idxs = sorted(ds.items(), key=itemgetter(0))[0]
            if len(idxs) == 1:
                grid[(x, y)] = idxs[0]
            else:
                grid[(x, y)] = -1


    edge = set()
    for z in range(MIN_GRID, MAX_GRID+1):
        edge.add(grid[(MIN_GRID, z)])
        edge.add(grid[(MAX_GRID, z)])
        edge.add(grid[(z, MIN_GRID)])
        edge.add(grid[(z, MAX_GRID)])

    return max(filter(lambda x: x[0] not in edge and x[0] != -1, Counter(grid.values()).items()), key=itemgetter(1))[1]


def solve_part_two():
    coords = parse_input()
    area_size = 0

    for x in range(MIN_GRID, MAX_GRID+1):
        for y in range(MIN_GRID, MAX_GRID+1):
            total_d = sum(dist(x, y, a, b) for a, b in coords)
            if total_d < TOTAL_DIST_LIMIT:
                area_size += 1

    return grid


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
