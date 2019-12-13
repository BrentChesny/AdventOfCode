from intcode import IntCodeProcessor
from collections import defaultdict


def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))


def run(program, input):
    computer = IntCodeProcessor(program, input)
    screen = defaultdict(int)
    paddle_pos = (0, 0)
    ball_pos = (0, 0)
    score = 0

    while not computer.is_halted():
        output = computer.execute()

        while output:
            x, y, tile, output = output[0], output[1], output[2], output[3:]

            if x >= 0:
                screen[(x, y)] = tile

                if tile == 4:
                    ball_pos = (x, y)
                    paddle_x, _ = paddle_pos
                    dx = paddle_x - x
                    if dx < 0:
                        input.append(1)
                    elif dx > 0:
                        input.append(-1)
                    else:
                        input.append(0)
                if tile == 3:
                    paddle_pos = (x, y)
            else:
                score = tile

    return screen, score


def draw(screen):
    if not screen:
        return
    min_x = min(x for x, y in screen.keys())
    min_y = min(y for x, y in screen.keys())
    max_x = max(x for x, y in screen.keys())
    max_y = max(y for x, y in screen.keys())

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if screen[(x, y)] == 1:
                tile = '|'
            elif screen[(x, y)] == 2:
                tile = '#'
            elif screen[(x, y)] == 3:
                tile = '-'
            elif screen[(x, y)] == 4:
                tile = 'O'
            else:
                tile = ' '
            print(tile, end='')
        print()


def solve_part_one():
    program = parse_input()
    screen, _ = run(program, [])
    return len([tile for tile in screen.values() if tile == 2])


def solve_part_two():
    program = parse_input()
    program[0] = 2
    _, score = run(program, [])
    return score


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
