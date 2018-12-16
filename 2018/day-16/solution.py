OPS = {
    'addr': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] + r[i[2]] for j in range(4)),
    'addi': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] + i[2] for j in range(4)),
    'mulr': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] * r[i[2]] for j in range(4)),
    'muli': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] * i[2] for j in range(4)),
    'banr': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] & r[i[2]] for j in range(4)),
    'bani': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] & i[2] for j in range(4)),
    'borr': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] | r[i[2]] for j in range(4)),
    'bori': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] | i[2] for j in range(4)),
    'setr': lambda r, i: tuple(r[j] if j != i[3] else r[i[1]] for j in range(4)),
    'seti': lambda r, i: tuple(r[j] if j != i[3] else i[1] for j in range(4)),
    'gtir': lambda r, i: tuple(r[j] if j != i[3] else int(i[1] > r[i[2]]) for j in range(4)),
    'gtri': lambda r, i: tuple(r[j] if j != i[3] else int(r[i[1]] > i[2]) for j in range(4)),
    'gtrr': lambda r, i: tuple(r[j] if j != i[3] else int(r[i[1]] > r[i[2]]) for j in range(4)),
    'eqir': lambda r, i: tuple(r[j] if j != i[3] else int(i[1] == r[i[2]]) for j in range(4)),
    'eqri': lambda r, i: tuple(r[j] if j != i[3] else int(r[i[1]] == i[2]) for j in range(4)),
    'eqrr': lambda r, i: tuple(r[j] if j != i[3] else int(r[i[1]] == r[i[2]]) for j in range(4)),
}


def parse_input():
    raw = open('input.txt').read()
    samples, program = raw.split('\n\n\n')
    samples = [sample.split('\n') for sample in samples.split('\n\n')]
    samples = [(tuple(eval(before[8:])), tuple(map(int, instruction.split(' '))), tuple(eval(after[7:]))) for before, instruction, after in samples]
    program = [tuple(map(int, instruction.split(' '))) for instruction in program.strip().split('\n')]
    return samples, program

def try_sample(sample):
    possible_ops = set()
    before, instruction, after = sample
    for opname, op in OPS.items():
        computed_after = op(before, instruction)
        if after == computed_after:
            possible_ops.add(opname)
    return possible_ops

def figure_out_opcodes(samples):
    opcodes = {i: set(OPS.keys()) for i in range(16)}

    for sample in samples:
        _, (opcode, _, _, _), _ = sample
        possible_ops = try_sample(sample)
        opcodes[opcode] &= possible_ops

    while not all(len(ops) == 1 for opcode, ops in opcodes.items()):
        decided = {op for ops in opcodes.values() if len(ops) == 1 for op in ops}
        for ops in opcodes.values():
            if len(ops) > 1:
                ops -= decided

    return {opcode: op for opcode, ops in opcodes.items() for op in ops}

def execute_program(program, opcodes):
    registers = (0, 0, 0, 0)
    for instruction in program:
        opcode = instruction[0]
        registers = OPS[opcodes[opcode]](registers, instruction)
    return registers


def solve_part_one():
    samples, _ = parse_input()
    result = 0
    for sample in samples:
        if len(try_sample(sample)) >= 3:
            result += 1
    return result


def solve_part_two():
    samples, program = parse_input()
    opcodes = figure_out_opcodes(samples)
    registers = execute_program(program, opcodes)
    return registers[0]


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
