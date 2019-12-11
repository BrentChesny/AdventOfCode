from intcode import IntCodeProcessor
from collections import defaultdict

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))


def paint(starting_color=0):
    program = parse_input()
    input = []
    robot = IntCodeProcessor(program, input)
    panels = defaultdict(int)
    current_dir = 0
    x, y = 0, 0

    panels[(x, y)] = starting_color

    while not robot.is_halted():
        current_color = panels[(x, y)]
        input.append(current_color)

        new_color, turn = robot.execute()

        panels[(x, y)] = new_color

        if turn == 0:
            current_dir = (current_dir - 1) % 4
        elif turn == 1:
            current_dir = (current_dir + 1) % 4
        else:
            assert False

        dx, dy = DIRS[current_dir]
        x, y = x + dx, y + dy

    return panels


def draw(panels):
    min_x = min(x for x, y in panels.keys())
    min_y = min(y for x, y in panels.keys())
    max_x = max(x for x, y in panels.keys())
    max_y = max(y for x, y in panels.keys())

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            print('#' if panels[(x, y)] == 1 else ' ', end='')
        print()


def solve_part_one():
    return len(paint())


def solve_part_two():
    panels = paint(1)
    draw(panels)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ')
    solve_part_two()


if __name__ == '__main__':
    main()
