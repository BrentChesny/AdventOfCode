from intcode import IntCodeProcessor


def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))


def solve_part_one():
    program = parse_input()
    return IntCodeProcessor(program, [1]).execute()[-1]


def solve_part_two():
    program = parse_input()
    return IntCodeProcessor(program, [2]).execute()[-1]


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
