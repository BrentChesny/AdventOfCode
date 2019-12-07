from intcode import IntCodeProcessor
from itertools import permutations


def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))


def run_amplifiers(program, phases):
    amps = [IntCodeProcessor(program, [phase]) for phase in phases]
    amps[0].input.append(0)
    output = None
    while not all(amp.is_halted() for amp in amps):
        for i, amp in enumerate(amps):
            output = amp.execute()
            amps[(i+1) % 5].input.extend(output)
    return output[-1]


def solve_part_one():
    program = parse_input()
    phases = [0, 1, 2, 3, 4]
    return max(run_amplifiers(program, conf) for conf in permutations(phases))


def solve_part_two():
    program = parse_input()
    phases = [5, 6, 7, 8, 9]
    return max(run_amplifiers(program, conf) for conf in permutations(phases))


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
