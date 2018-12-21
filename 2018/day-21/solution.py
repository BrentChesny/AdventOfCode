from collections import defaultdict

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


def solve_part_one():
    binding, program = parse_input()
    registers = (0, 0, 0, 0, 0, 0)
    ip = 0
    while True:
        try:
            instruction = program[ip]
            registers = tuple(registers[j] if j != binding else ip for j in range(N_REGISTERS))
            opcode = instruction[0]
            if opcode == 'eqrr':
                return registers[instruction[1]]
            registers = OPS[opcode](registers, instruction)
            ip = registers[binding]
            ip += 1
        except IndexError:
            break

def solve_part_two():
    # Tip: run this wiht pypy to avoid waiting a lifetime
    binding, program = parse_input()
    registers = (0, 0, 0, 0, 0, 0)
    ip = 0
    seen = set()
    last_value = None
    while True:
        try:
            instruction = program[ip]
            registers = tuple(registers[j] if j != binding else ip for j in range(N_REGISTERS))
            opcode = instruction[0]
            if opcode == 'eqrr':
                if registers[instruction[1]] in seen:
                    return last_value
                seen.add(registers[instruction[1]])
                last_value = registers[instruction[1]]
            registers = OPS[opcode](registers, instruction)
            ip = registers[binding]
            ip += 1
        except IndexError:
            break


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
