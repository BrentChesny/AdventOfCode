from collections import defaultdict
from math import sqrt

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
    result = 0

    while 0 <= pc < len(instructions):
        instruction, args = instructions[pc]
        if instruction == 'set':
            regs[args[0]] = parse_val(args[1], regs)
        elif instruction == 'sub':
            regs[args[0]] -= parse_val(args[1], regs)
        elif instruction == 'mul':
            regs[args[0]] *= parse_val(args[1], regs)
            result += 1
        elif instruction == 'jnz':
            if parse_val(args[0], regs) != 0:
                pc += (parse_val(args[1], regs) - 1)
        pc += 1

    return result

def solve_part_two():
    b = 106700
    c = 123700
    h = 0
    for x in xrange(b, c+1, 17):
        for a in xrange(2, x):
            if x % a == 0:
                h += 1
                break
    return h

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
