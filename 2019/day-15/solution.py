from intcode import IntCodeProcessor
from collections import defaultdict

DIR_DELTAS = {
    1: (0, -1),
    2: (0, 1),
    3: (-1, 0),
    4: (1, 0),
}

NEXT_DIRS = {
    1: [3, 1, 4, 2],
    2: [4, 2, 3, 1],
    3: [2, 3, 1, 4],
    4: [1, 4, 2, 3],
}

DIRS = [1, 2, 3, 4]


def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))


def explore():
    program = parse_input()
    input = []
    computer = IntCodeProcessor(program, input)

    map = {(0, 0): '.'}
    current_dir = 1
    x, y = 0, 0
    exploration_steps = 0

    while exploration_steps < 40000:
        exploration_steps += 1
        for dir in NEXT_DIRS[current_dir]:
            dx, dy = DIR_DELTAS[dir]
            if (x+dx, y+dy) not in map or map[(x+dx, y+dy)] == '.':
                current_dir = dir
                break

        input.append(current_dir)
        dx, dy = DIR_DELTAS[current_dir]

        output = computer.execute()

        if output:
            status = output[0]
            if status == 0:
                map[(x+dx, y+dy)] = '#'
            elif status == 1:
                x += dx
                y += dy
                map[(x, y)] = '.'
            elif status == 2:
                x += dx
                y += dy
                map[(x, y)] = 'O'
    return map


def draw(map, px, py):
    min_x = min(x for x, y in map.keys())
    min_y = min(y for x, y in map.keys())
    max_x = max(x for x, y in map.keys())
    max_y = max(y for x, y in map.keys())

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if x == px and y == py:
                print('X', end='')
            else:
                print(map[(x, y)] if (x, y) in map else ' ', end='')
        print()


def shortest_distance(map):
    queue = [(0, 0, 0)]
    seen = set()
    while queue:
        x, y, d = queue.pop(0)
        seen.add((x, y))
        for dir in DIRS:
            dx, dy = DIR_DELTAS[dir]
            if (x+dx, y+dy) in seen:
                continue
            if (x+dx, y+dy) in map and map[(x+dx, y+dy)] == 'O':
                return d+1
            if (x+dx, y+dy) in map and map[(x+dx, y+dy)] == '.':
                queue.append((x+dx, y+dy, d+1))


def oxygen_time(map):
    time = 0
    while sum(v == '.' for v in map.values()):
        new_map = map.copy()
        for x, y in map:
            if map[(x, y)] == '.':
                for dx, dy in DIR_DELTAS.values():
                    if (x+dx, y+dy) in map and map[(x+dx, y+dy)] == 'O':
                        new_map[(x, y)] = 'O'
                        break
        map = new_map
        time += 1
    return time


def solve_part_one():
    map = explore()
    return shortest_distance(map)


def solve_part_two():
    map = explore()
    return oxygen_time(map)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
