from intcode import IntCodeProcessor
from collections import defaultdict


def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))


def is_in_beam(program, x, y):
    calculator = IntCodeProcessor(program, [x, y])
    output = calculator.execute()
    return output[0] == 1


def solve_part_one():
    program = parse_input()

    in_beam = 0
    for x in range(50):
        for y in range(50):
            if is_in_beam(program, x, y):
                in_beam += 1

    return in_beam


def solve_part_two():
    program = parse_input()
    x, y = 0, 0

    while True:
        while is_in_beam(program, x+1, y):
            x += 1
        if is_in_beam(program, x-99, y) and is_in_beam(program, x-99, y+99):
            return (x-99) * 10000 + y
        y += 1


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
