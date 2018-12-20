from collections import deque

def parse_input():
    return open('input.txt').read().strip()[1:-1]

def show(grid):
    min_x = min(x for x, y in grid)
    max_x = max(x for x, y in grid)
    min_y = min(y for x, y in grid)
    max_y = max(y for x, y in grid)

    for y in range(max_y + 1, min_y - 2, -1):
        row = ''
        for x in range(min_x - 1, max_x + 2):
            if (x, y) == (0, 0):
                row += 'X'
            else:
                row += grid.get((x, y), '#')
        print(row)

def explore(regex):
    x, y = 0, 0
    grid = {
        (x, y): '.'
    }
    stack = []

    for c in regex:
        if c == 'N':
            grid[(x, y + 1)] = '.'
            grid[(x, y + 2)] = '.'
            y += 2
        elif c == 'S':
            grid[(x, y - 1)] = '.'
            grid[(x, y - 2)] = '.'
            y -= 2
        elif c == 'E':
            grid[(x + 1, y)] = '.'
            grid[(x + 2, y)] = '.'
            x += 2
        elif c == 'W':
            grid[(x - 1, y)] = '.'
            grid[(x - 2, y)] = '.'
            x -= 2
        elif c == '(':
            stack.append((x, y))
        elif c == ')':
            x, y = stack.pop()
        elif c == '|':
            x, y = stack.pop()
            stack.append((x, y))
    return grid

def calculate_distances(grid):
    start = (0, 0)
    visiting = deque([(start, 0)])
    dists = {start: 0}
    seen = set()

    while visiting:
        pos, dist = visiting.popleft()
        dists[pos] = dist
        x, y = pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            door_or_wall = x + dx, y + dy
            next_pos= x + 2*dx, y + 2*dy
            if grid.get(door_or_wall, '#') == '#':
                continue
            if next_pos in seen:
                continue
            if not any(next == visit[0] for visit in visiting):
                visiting.append((next_pos, dist + 1))
        seen.add(pos)

    return dists

def solve_part_one():
    regex = parse_input()
    grid = explore(regex)
    return max(calculate_distances(grid).values())

def solve_part_two():
    regex = parse_input()
    grid = explore(regex)
    return len([dist for dist in calculate_distances(grid).values() if dist >= 1000])


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
