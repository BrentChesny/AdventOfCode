import re

def parse_input():
    points = [tuple(map(int, re.findall(r'\-?\d+', line))) for line in open('input.txt')]
    positions = [(x, y) for x, y, _, _ in points]
    velocities = [(vx, vy) for _, _, vx, vy in points]
    return positions, velocities

def positions_at_time(positions, velocities, time):
    new_positions = []
    for (x, y), (vx, vy) in zip(positions, velocities):
        new_x = x + time * vx
        new_y = y + time * vy

        new_positions.append((new_x, new_y))
    return new_positions

def solve():
    positions, velocities = parse_input()
    widths = []

    for time in range(20000):
        new_positions = positions_at_time(positions, velocities, time)

        xs, _ = zip(*new_positions)
        widths.append(max(xs) - min(xs))

    min_time = widths.index(min(widths))

    min_positions = positions_at_time(positions, velocities, min_time)
    xs, ys = zip(*min_positions)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    print('Part one: ')
    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            if ((x, y) in min_positions):
                line += '#'
            else:
                line += ' '
        print(line)

    return min_time


def main():
    print('Part two: ', solve())


if __name__ == '__main__':
    main()
