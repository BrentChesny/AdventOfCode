from math import sqrt

N_REGISTERS = 6

OPS = {
    'addr': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] + r[i[2]] for j in range(N_REGISTERS)),
    'addi': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] + i[2] for j in range(N_REGISTERS)),
    'mulr': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] * r[i[2]] for j in range(N_REGISTERS)),
    'muli': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] * i[2] for j in range(N_REGISTERS)),
    'banr': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] & r[i[2]] for j in range(N_REGISTERS)),
    'bani': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] & i[2] for j in range(N_REGISTERS)),
    'borr': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] | r[i[2]] for j in range(N_REGISTERS)),
    'bori': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] | i[2] for j in range(N_REGISTERS)),
    'setr': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] for j in range(N_REGISTERS)),
    'seti': lambda r, i: tuple(r[j] if j != i[3] else i[1] for j in range(N_REGISTERS)),
    'gtir': lambda r, i: tuple(r[j] if j != i[3] else int(i[1] > r[i[2]]) for j in range(N_REGISTERS)),
    'gtri': lambda r, i: tuple(r[j] if j != i[3] else int(r[i[1]] > i[2]) for j in range(N_REGISTERS)),
    'gtrr': lambda r, i: tuple(r[j] if j != i[3] else int(r[i[1]] > r[i[2]]) for j in range(N_REGISTERS)),
    'eqir': lambda r, i: tuple(r[j] if j != i[3] else int(i[1] == r[i[2]]) for j in range(N_REGISTERS)),
    'eqri': lambda r, i: tuple(r[j] if j != i[3] else int(r[i[1]] == i[2]) for j in range(N_REGISTERS)),
    'eqrr': lambda r, i: tuple(r[j] if j != i[3] else int(r[i[1]] == r[i[2]]) for j in range(N_REGISTERS)),
}


def parse_input():
    raw = open('input.txt').read().strip()
    lines = raw.split('\n')
    binding, program = lines[0], lines[1:]
    binding = int(binding[4:])
    program = [instruction.split(' ') for instruction in program]
    program = [(opcode, int(a), int(b), int(c)) for opcode, a, b, c in program]
    return binding, program

def sum_of_factors(n):
    s = 0
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            s += x
            s += n // x
    return s

def solve_part_one():
    binding, program = parse_input()
    registers = (0, 0, 0, 0, 0, 0)
    ip = 0

    while True:
        try:
            instruction = program[ip]
            registers = tuple(registers[j] if j != binding else ip for j in range(N_REGISTERS))
            opcode = instruction[0]
            registers = OPS[opcode](registers, instruction)
            ip = registers[binding]
            ip += 1
        except IndexError:
            break

    return registers[0]

def solve_part_two():
    binding, program = parse_input()
    registers = (1, 0, 0, 0, 0, 0)
    ip = 0

    while True:
        try:
            instruction = program[ip]
            registers = tuple(registers[j] if j != binding else ip for j in range(N_REGISTERS))

            # The loop at ip = 2 seems to calculate the sum of the factors of the value in r5.
            # This value is significantly larger when r0 is set to 1 at the start.
            # So when we encounter that loop, let's just calculate the sum of the factors directly.
            if ip == 3:
                return sum_of_factors(registers[5])

            opcode = instruction[0]
            registers = OPS[opcode](registers, instruction)
            ip = registers[binding]
            ip += 1
        except IndexError:
            break

    return registers


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
