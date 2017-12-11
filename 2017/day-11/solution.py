coord_map = {
    'n': (0, 1, -1),
    'ne': (1, 0, -1),
    'se': (1, -1, 0),
    's': (0, -1, 1),
    'sw': (-1, 0, 1),
    'nw': (-1, 1, 0),
}

def solve_part_one():
    steps = open('input.txt').read().strip().split(',')
    x, y, z = 0, 0, 0

    for step in steps:
        dx, dy, dz = coord_map[step]
        x, y, z = x + dx, y + dy, z + dz

    return (abs(x) + abs(y) + abs(z)) / 2


def solve_part_two():
    steps = open('input.txt').read().strip().split(',')
    x, y, z = 0, 0, 0
    dists = []

    for step in steps:
        dx, dy, dz = coord_map[step]
        x, y, z = x + dx, y + dy, z + dz
        dists.append((abs(x) + abs(y) + abs(z)) / 2)

    return max(dists)


def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
