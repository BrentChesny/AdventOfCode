from intcode import IntCodeProcessor
from collections import defaultdict


def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))


def run_script(script):
    program = parse_input()

    input = []
    for line in script:
        for c in line:
            input.append(ord(c))
        input.append(10)

    droid = IntCodeProcessor(program, input)
    while not droid.is_halted():
        output = droid.execute()
        for c in output:
            if c > 255:
                return c


def solve_part_one():
    script = []
    script.append('NOT A J')
    script.append('NOT B T')
    script.append('OR T J')
    script.append('NOT C T')
    script.append('OR T J')
    script.append('AND D J')
    script.append('WALK')
    return run_script(script)


def solve_part_two():
    script = []
    script.append('NOT A J')
    script.append('NOT B T')
    script.append('OR T J')
    script.append('NOT C T')
    script.append('OR T J')
    script.append('AND D J')
    script.append('NOT E T')
    script.append('NOT T T')
    script.append('OR H T')
    script.append('AND T J')
    script.append('RUN')
    return run_script(script)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
