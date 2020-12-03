from intcode import IntCodeProcessor
from collections import defaultdict


def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))


def is_intersection(scaffold, x, y):
    return (x-1, y) in scaffold and (x+1, y) in scaffold and (x, y-1) in scaffold and (x, y+1) in scaffold


def solve_part_one():
    program = parse_input()
    input = []
    computer = IntCodeProcessor(program, input)

    scaffold = set()

    while not computer.is_halted():
        output = computer.execute()

        x, y = 0, 0
        for c in output:
            if chr(c) == '#':
                scaffold.add((x, y))
            if chr(c) == '\n':
                x = 0
                y += 1
            else:
                x += 1

    return sum(x*y for x, y in scaffold if is_intersection(scaffold, x, y))


def solve_part_two():
    program = parse_input()
    program[0] = 2
    input = []
    computer = IntCodeProcessor(program, input)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
