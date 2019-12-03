directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}


def parse_input():
    return [[(step[0], int(step[1:])) for step in line.split(',')]
            for line in open('input.txt').readlines()]


def calculate_positions(wire):
    positions = set()
    step_map = dict()
    x, y = 0, 0
    step_count = 0
    for dir, steps in wire:
        dx, dy = directions[dir]
        for _ in range(steps):
            step_count += 1
            x, y = x+dx, y+dy
            positions.add((x, y))
            if (x, y) not in step_map:
                step_map[(x, y)] = step_count
    return positions, step_map


def dist(pos):
    x, y = pos
    return abs(x) + abs(y)


def solve_part_one():
    wire_a, wire_b = parse_input()
    positions_a, _ = calculate_positions(wire_a)
    positions_b, _ = calculate_positions(wire_b)

    intersections = positions_a.intersection(positions_b)

    return min(dist(pos) for pos in intersections)


def solve_part_two():
    wire_a, wire_b = parse_input()
    positions_a, step_map_a = calculate_positions(wire_a)
    positions_b, step_map_b = calculate_positions(wire_b)

    intersections = positions_a.intersection(positions_b)

    return min(step_map_a[intersection] + step_map_b[intersection] for intersection in intersections)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
