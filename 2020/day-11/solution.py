from os import readlink


def parse_input():
    return [list(line) for line in open("input.txt").read().splitlines()]


def step(grid):
    copy = [r[:] for r in grid]
    h = len(copy)
    w = len(copy[0])
    for r in range(h):
        for c in range(w):
            occ = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == dc == 0:
                        continue
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < h and 0 <= cc < w:
                        occ += 1 if grid[rr][cc] == "#" else 0
            if grid[r][c] == "L" and occ == 0:
                copy[r][c] = "#"
            elif grid[r][c] == "#" and occ >= 4:
                copy[r][c] = "L"
    return copy


dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (-1, 1),
    (-1, -1),
    (1, -1),
]


def step_two(grid):
    copy = [r[:] for r in grid]
    h = len(copy)
    w = len(copy[0])
    for r in range(h):
        for c in range(w):
            occ = 0
            for dr, dc in dirs:
                for i in range(1, max(w, h)):
                    rr, cc = r + i * dr, c + i * dc
                    if not (0 <= rr < h and 0 <= cc < w):
                        break
                    if grid[rr][cc] == "#":
                        occ += 1
                        break
                    if grid[rr][cc] == "L":
                        break
            if grid[r][c] == "L" and occ == 0:
                copy[r][c] = "#"
            elif grid[r][c] == "#" and occ >= 5:
                copy[r][c] = "L"
    return copy


def serialize(grid):
    return "".join(["".join(r) for r in grid])


def solve_part_one():
    grid = parse_input()
    seen = set()
    while True:
        seen.add(serialize(grid))
        grid = step(grid)
        if serialize(grid) in seen:
            return serialize(grid).count("#")


def solve_part_two():
    grid = parse_input()
    seen = set()
    while True:
        seen.add(serialize(grid))
        grid = step_two(grid)
        if serialize(grid) in seen:
            return serialize(grid).count("#")


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
