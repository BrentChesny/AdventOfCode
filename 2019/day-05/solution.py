ADD = 1
MUL = 2
IN = 3
OUT = 4
JIT = 5
JIF = 6
LT = 7
EQ = 8

n_args = {
 ADD: 3,
 MUL: 3,
 IN: 1,
 OUT: 1,
 JIT: 2,
 JIF: 2,
 LT: 3,
 EQ: 3,
}

def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))

def pad(l, width):
    l.extend([0] * (width - len(l)))
    return l

def decode_opcode(opcode):
    instruction = opcode % 100
    params = opcode // 100
    modes = list(map(int, reversed(str(params))))
    return instruction, pad(modes, n_args[instruction])

def get_param(program, ip, i, immediate_mode=True):
    param = program[ip+i]
    if immediate_mode:
        return param
    return program[param]

def execute(program, input):
    ip = 0
    output = []

    while program[ip] != 99:
        opcode = program[ip]
        instruction, modes = decode_opcode(opcode)
        if instruction == ADD:
            program[get_param(program, ip, 3)] = get_param(program, ip, 1, modes[0]) + get_param(program, ip, 2, modes[1])
            ip += len(modes) + 1
        elif instruction == MUL:
            program[get_param(program, ip, 3)] = get_param(program, ip, 1, modes[0]) * get_param(program, ip, 2, modes[1])
            ip += len(modes) + 1
        elif instruction == IN:
            program[get_param(program, ip, 1)] = input.pop(0)
            ip += len(modes) + 1
        elif instruction == OUT:
            output.append(get_param(program, ip, 1, modes[0]))
            ip += len(modes) + 1
        elif instruction == JIT:
            if get_param(program, ip, 1, modes[0]):
                ip = get_param(program, ip, 2, modes[1])
            else:
                ip += len(modes) + 1
        elif instruction == JIF:
            if not get_param(program, ip, 1, modes[0]):
                ip = get_param(program, ip, 2, modes[1])
            else:
                ip += len(modes) + 1
        elif instruction == LT:
            program[get_param(program, ip, 3)] = 1 if get_param(program, ip, 1, modes[0]) < get_param(program, ip, 2, modes[1]) else 0
            ip += len(modes) + 1
        elif instruction == EQ:
            program[get_param(program, ip, 3)] = 1 if get_param(program, ip, 1, modes[0]) == get_param(program, ip, 2, modes[1]) else 0
            ip += len(modes) + 1

    return output[-1]

def solve_part_one():
    program = parse_input()
    return execute(program, [1])

def solve_part_two():
    program = parse_input()
    return execute(program, [5])


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())

if __name__ == '__main__':
    main()
