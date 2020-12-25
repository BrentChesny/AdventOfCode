from collections import defaultdict


def parse_input():
    return list(map(parse_line, open("input.txt").read().splitlines()))


def parse_line(line):
    steps = []
    buffer = ""
    for c in line:
        if c in ["e", "w"]:
            buffer += c
            steps.append(buffer)
            buffer = ""
        else:
            buffer += c
    return steps


deltas = {
    "e": (2, 0),
    "w": (-2, 0),
    "ne": (1, 1),
    "se": (1, -1),
    "nw": (-1, 1),
    "sw": (-1, -1),
}


def initial_black_tiles(paths):
    colors = defaultdict(int)

    for steps in paths:
        x, y = (0, 0)
        for step in steps:
            dx, dy = deltas[step]
            x, y = x + dx, y + dy
        colors[(x, y)] = 1 if colors[(x, y)] == 0 else 0

    return {tile for tile, color in colors.items() if color == 1}


def solve_part_one():
    paths = parse_input()
    return len(initial_black_tiles(paths))


def all_neighbours(tiles):
    return set.union(*[neighbours(t) for t in tiles])


def neighbours(tile):
    x, y = tile
    return {(x + dx, y + dy) for dx, dy in deltas.values()}


def step(tiles):
    new_tiles = set()
    for p in tiles:
        n = neighbours(p)
        tiles_n = n.intersection(tiles)
        if 1 <= len(tiles_n) <= 2:
            new_tiles.add(p)

    for n in all_neighbours(tiles):
        if n in tiles:
            continue
        m = neighbours(n)
        tiles_m = m.intersection(tiles)
        if len(tiles_m) == 2:
            new_tiles.add(n)
    return new_tiles


def solve_part_two():
    paths = parse_input()
    tiles = initial_black_tiles(paths)

    for _ in range(100):
        tiles = step(tiles)
    return len(tiles)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
