NEIGHBOURS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def parse_input():
    return [list(line.strip()) for line in open("input.txt").readlines()]


def empty():
    return [["." for _ in range(5)] for _ in range(5)]


def step(universe):
    R = len(universe)
    C = len(universe[0])
    new_universe = [r[:] for r in universe]
    for r in range(R):
        for c in range(C):
            n = 0
            for dr, dc in NEIGHBOURS:
                if (
                    0 <= r + dr < R
                    and 0 <= c + dc < C
                    and universe[r + dr][c + dc] == "#"
                ):
                    n += 1
            if universe[r][c] == "#" and n != 1:
                new_universe[r][c] = "."
            elif universe[r][c] == "." and n in [1, 2]:
                new_universe[r][c] = "#"
    return new_universe


def count_bugs_on_top(grid):
    return grid[0].count("#")


def count_bugs_on_bottom(grid):
    return grid[4].count("#")


def count_bugs_on_left(grid):
    return [row[0] for row in grid].count("#")


def count_bugs_on_right(grid):
    return [row[4] for row in grid].count("#")


def count_bugs(grid):
    return sum(row.count("#") for row in grid)


def step_multi_dimensional(universes, depth):
    new_universes = dict()
    new_universes[-depth] = empty()
    new_universes[depth] = empty()
    for level in range(-depth + 1, depth):
        universe = universes[level]
        R = len(universe)
        C = len(universe[0])
        new_universe = [r[:] for r in universe]
        for r in range(R):
            for c in range(C):
                if r == 2 and c == 2:
                    continue
                n = 0
                for dr, dc in NEIGHBOURS:
                    if (
                        0 <= r + dr < R
                        and 0 <= c + dc < C
                        and universe[r + dr][c + dc] == "#"
                        and not (r + dr == 2 and c + dc == 2)
                    ):
                        n += 1
                if r == 0:
                    # tile has neighbor at level - 1 at the inner middle top
                    n += 1 if universes[level - 1][1][2] == "#" else 0
                if r == 4:
                    # tile has neighbor at level - 1 at the inner middle bottom
                    n += 1 if universes[level - 1][3][2] == "#" else 0
                if c == 0:
                    # tile has neighbor at level - 1 at the inner middle left
                    n += 1 if universes[level - 1][2][1] == "#" else 0
                if c == 4:
                    # tile has neighbor at level - 1 at the inner middle right
                    n += 1 if universes[level - 1][2][3] == "#" else 0

                if r == 1 and c == 2:
                    # tile has neighbor at level + 1 at the outer top
                    n += count_bugs_on_top(universes[level + 1])
                elif r == 3 and c == 2:
                    # tile has neighbor at level + 1 at the outer bottom
                    n += count_bugs_on_bottom(universes[level + 1])
                elif c == 1 and r == 2:
                    # tile has neighbor at level + 1 at the outer left
                    n += count_bugs_on_left(universes[level + 1])
                elif c == 3 and r == 2:
                    # tile has neighbor at level + 1 at the outer right
                    n += count_bugs_on_right(universes[level + 1])

                if universe[r][c] == "#" and n != 1:
                    new_universe[r][c] = "."
                elif universe[r][c] == "." and n in [1, 2]:
                    new_universe[r][c] = "#"
        new_universes[level] = new_universe
    return new_universes


def serialize(universe):
    return tuple(map(tuple, universe))


def biodiversity(universe):
    R = len(universe)
    C = len(universe[0])

    score = 0
    multiplier = 1
    for r in range(R):
        for c in range(C):
            if universe[r][c] == "#":
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
    universe = parse_input()
    universes = {0: universe}
    depth = 200

    for level in range(1, depth + 1):
        universes[level] = empty()
        universes[-level] = empty()

    for _ in range(200):
        universes = step_multi_dimensional(universes, depth)

    total = 0
    for grid in universes.values():
        total += count_bugs(grid)
    return total


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
