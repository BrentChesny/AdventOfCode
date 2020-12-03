NEIGHBOURS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def parse_input():
    return [list(line.strip()) for line in open('input.txt').readlines()]


def step(universe):
    R = len(universe)
    C = len(universe[0])
    new_universe = [r[:] for r in universe]
    for r in range(R):
        for c in range(C):
            n = 0
            for dr, dc in NEIGHBOURS:
                if 0 <= r + dr < R and 0 <= c + dc < C and universe[r+dr][c+dc] == '#':
                    n += 1
            if universe[r][c] == '#' and n != 1:
                new_universe[r][c] = '.'
            elif universe[r][c] == '.' and n in [1, 2]:
                new_universe[r][c] = '#'
    return new_universe


def serialize(universe):
    return tuple(map(tuple, universe))


def biodiversity(universe):
    R = len(universe)
    C = len(universe[0])

    score = 0
    multiplier = 1
    for r in range(R):
        for c in range(C):
            if universe[r][c] == '#':
                score += multiplier
            multiplier *= 2
    return score


def solve_part_one():
    universe = parse_input()
    seen = set()

    while serialize(universe) not in seen:
        seen.add(serialize(universe))
        universe = step(universe)

    return biodiversity(universe)


def solve_part_two():
    pass


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
