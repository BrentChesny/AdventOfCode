from collections import defaultdict

def parse_input():
    instructions = []
    for line in open('input.txt').readlines():
        parts = line.strip().split()
        instruction, args = parts[0], parts[1:]
        instructions.append((instruction, args))
    return instructions


def solve_part_one():
    instructions = parse_input()
    regs = defaultdict(int)
    pc = 0
    freq = None

    while 0 <= pc < len(instructions):
        instruction, args = instructions[pc]
        if instruction == 'snd':
            freq = parse_val(args[0], regs)
        elif instruction == 'set':
            regs[args[0]] = parse_val(args[1], regs)
        elif instruction == 'add':
            regs[args[0]] += parse_val(args[1], regs)
        elif instruction == 'mul':
            regs[args[0]] *= parse_val(args[1], regs)
        elif instruction == 'mod':
            regs[args[0]] %= parse_val(args[1], regs)
        elif instruction == 'rcv':
            if parse_val(args[0], regs) != 0:
                return freq
        elif instruction == 'jgz':
            if parse_val(args[0], regs) > 0:
                pc += (parse_val(args[1], regs) - 1)
        pc += 1


def solve_part_two():
    instructions = parse_input()
    regs_0, pc_0 = defaultdict(int), 0
    regs_1, pc_1 = defaultdict(int), 0
    regs_0['p'], regs_1['p'] = 0, 1
    buffer_0, buffer_1 = [], []
    change_0, change_1 = True, True
    result = 0

    while change_0 or change_1:
        change_0, change_1 = False, False
        while instructions[pc_0][0] != 'rcv' or buffer_0:
            instruction, args = instructions[pc_0]
            if instruction == 'snd':
                buffer_1.append(parse_val(args[0], regs_0))
            elif instruction == 'set':
                regs_0[args[0]] = parse_val(args[1], regs_0)
            elif instruction == 'add':
                regs_0[args[0]] += parse_val(args[1], regs_0)
            elif instruction == 'mul':
                regs_0[args[0]] *= parse_val(args[1], regs_0)
            elif instruction == 'mod':
                regs_0[args[0]] %= parse_val(args[1], regs_0)
            elif instruction == 'rcv':
                regs_0[args[0]] = buffer_0.pop(0)
            elif instruction == 'jgz':
                if parse_val(args[0], regs_0) > 0:
                    pc_0 += (parse_val(args[1], regs_0) - 1)
            pc_0 += 1
            change_0 = True

        while instructions[pc_1][0] != 'rcv' or buffer_1:
            instruction, args = instructions[pc_1]
            if instruction == 'snd':
                buffer_0.append(parse_val(args[0], regs_1))
                result += 1
            elif instruction == 'set':
                regs_1[args[0]] = parse_val(args[1], regs_1)
            elif instruction == 'add':
                regs_1[args[0]] += parse_val(args[1], regs_1)
            elif instruction == 'mul':
                regs_1[args[0]] *= parse_val(args[1], regs_1)
            elif instruction == 'mod':
                regs_1[args[0]] %= parse_val(args[1], regs_1)
            elif instruction == 'rcv':
                regs_1[args[0]] = buffer_1.pop(0)
            elif instruction == 'jgz':
                if parse_val(args[0], regs_1) > 0:
                    pc_1 += (parse_val(args[1], regs_1) - 1)
            pc_1 += 1
            change_1 = True

    return result

def parse_val(arg, regs):
    if arg.isalpha():
        return regs[arg]
    else:
        return int(arg)

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
