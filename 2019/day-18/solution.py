from collections import defaultdict
from string import ascii_uppercase, ascii_lowercase


def parse_grid(grid):
    doors = {}
    keys = {}
    start = None

    R = len(grid)
    C = len(grid[0])

    for r in range(R):
        for c in range(C):
            if grid[r][c] in ascii_lowercase:
                keys[(r, c)] = grid[r][c]
                grid[r][c] = '.'
            if grid[r][c] in ascii_uppercase:
                doors[(r, c)] = grid[r][c]
                grid[r][c] = '.'
            if grid[r][c] == '@':
                start = (r, c)
                grid[r][c] = '.'

    doors = {k: 1 << (ord(v)-ord('A')) for k, v in doors.items()}
    keys = {k: 1 << (ord(v)-ord('a')) for k, v in keys.items()}

    return grid, doors, keys, start


def parse_input():
    grid = [list(line.strip()) for line in open('input.txt').readlines()]
    return parse_grid(grid)


def parse_input_two():
    grid = [list(line.strip()) for line in open('input2.txt').readlines()]

    h = len(grid) // 2
    w = len(grid[0]) // 2

    q1 = [row[:w+1] for row in grid[:h+1]]
    q2 = [row[w:] for row in grid[:h+1]]
    q3 = [row[:w+1] for row in grid[h:]]
    q4 = [row[w:] for row in grid[h:]]

    return [
        parse_grid(q1),
        parse_grid(q2),
        parse_grid(q3),
        parse_grid(q4),
    ]


def bfs(grid, doors, keys, all_keys, start, collected_keys):
    queue = [(start, 0, collected_keys)]
    seen = set()
    while queue:
        pos, d, collected_keys = queue.pop(0)
        r, c = pos
        if pos in keys:
            collected_keys |= keys[pos]
            if collected_keys == all_keys:
                return d
        elif pos in doors and doors[pos] & collected_keys == 0:
            continue
        if (pos, collected_keys) not in seen:
            seen.add((pos, collected_keys))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = r+dr, c+dc
                new_pos = (new_r, new_c)
                if grid[new_r][new_c] != '#':
                    queue.append((new_pos, d + 1, collected_keys))


def solve_part_one():
    grid, doors, keys, start = parse_input()

    all_keys = 0
    for key in keys.values():
        all_keys |= key

    return bfs(grid, doors, keys, all_keys, start, 0)


def solve_part_two():
    parsed = parse_input_two()

    all_keys = 0
    for _, _, keys, _ in parsed:
        for key in keys.values():
            all_keys |= key

    answer = 0
    for grid, doors, keys, start in parsed:
        collected_keys = all_keys
        for key in keys.values():
            collected_keys ^= key

        answer += bfs(grid, doors, keys, all_keys, start, collected_keys)

    return answer


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
