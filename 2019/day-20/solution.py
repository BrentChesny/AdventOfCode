from string import ascii_uppercase
from collections import defaultdict

OUTER = 0
INNER = 1


def parse_input():
    grid = [[c for c in line.rstrip()] for line in open('input.txt').readlines()]
    portals = defaultdict(list)
    start = None
    end = None

    middle = len(grid)/2

    R = len(grid)
    for r in range(R):
        for c in range(len(grid[r])):
            if grid[r][c] == '.':
                if grid[r-1][c] in ascii_uppercase:
                    # There is a portal above
                    key = grid[r-2][c] + grid[r-1][c]
                    if key == 'AA':
                        start = (r, c)
                    elif key == 'ZZ':
                        end = (r, c)
                    else:
                        portals[key].append(((r, c), OUTER if r < middle else INNER))
                elif grid[r+1][c] in ascii_uppercase:
                    # There is a portal below
                    key = grid[r+1][c] + grid[r+2][c]
                    if key == 'AA':
                        start = (r, c)
                    elif key == 'ZZ':
                        end = (r, c)
                    else:
                        portals[key].append(((r, c), INNER if r < middle else OUTER))
                elif grid[r][c-1] in ascii_uppercase:
                    # There is a portal left
                    key = grid[r][c-2] + grid[r][c-1]
                    if key == 'AA':
                        start = (r, c)
                    elif key == 'ZZ':
                        end = (r, c)
                    else:
                        portals[key].append(((r, c), OUTER if c < middle else INNER))
                elif grid[r][c+1] in ascii_uppercase:
                    # There is a portal right
                    key = grid[r][c+1] + grid[r][c+2]
                    if key == 'AA':
                        start = (r, c)
                    elif key == 'ZZ':
                        end = (r, c)
                    else:
                        portals[key].append(((r, c), INNER if c < middle else OUTER))

    return grid, portals, start, end


def solve_part_one():
    grid, portals, start, end = parse_input()

    queue = [(start, 0)]
    seen = set()
    while queue:
        pos, d = queue.pop(0)
        if pos == end:
            return d
        seen.add(pos)
        r, c = pos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r+dr, c+dc
            if grid[new_r][new_c] == '.' and (new_r, new_c) not in seen:
                queue.append(((new_r, new_c), d+1))
        for portal, dests in portals.items():
            dest = None
            if pos == dests[0][0]:
                dest = dests[1][0]
            elif pos == dests[1][0]:
                dest = dests[0][0]
            if dest and dest not in seen:
                queue.append((dest, d+1))


def solve_part_two():
    grid, portals, start, end = parse_input()

    queue = [(start, 0, 0)]
    seen = set()
    while queue:
        pos, l, d = queue.pop(0)
        if pos == end and l == 0:
            return d
        seen.add((pos, l))
        r, c = pos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r+dr, c+dc
            new_pos = new_r, new_c
            if grid[new_r][new_c] == '.' and (new_pos, l) not in seen:
                valid = True
                for portal, dests in portals.items():
                    if dests[0] == (new_pos, OUTER) or dests[1] == (new_pos, OUTER):
                        if l == 0:
                            valid = False
                if new_pos in [start, end] and l > 0:
                    valid = False
                if valid:
                    queue.append((new_pos, l, d+1))
        for portal, dests in portals.items():
            dest = None
            if (pos, OUTER) == dests[0]:
                if (dests[1][0], l-1) not in seen:
                    queue.append((dests[1][0], l-1, d+1))
            if (pos, INNER) == dests[0]:
                if (dests[1][0], l+1) not in seen:
                    queue.append((dests[1][0], l+1, d+1))
            if (pos, OUTER) == dests[1]:
                if (dests[0][0], l-1) not in seen:
                    queue.append((dests[0][0], l-1, d+1))
            if (pos, INNER) == dests[1]:
                if (dests[0][0], l+1) not in seen:
                    queue.append((dests[0][0], l+1, d+1))


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
