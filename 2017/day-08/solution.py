from collections import defaultdict

def solve_part_one():
    instructions = []
    for line in open('input.txt').readlines():
        reg, op, val, _, cond_reg, cond_op, cond_val = line.strip().split()
        val, cond_val = int(val), int(cond_val)
        instructions.append((reg, op, val, cond_reg, cond_op, cond_val))

    registers = defaultdict(int)
    for reg, op, val, cond_reg, cond_op, cond_val in instructions:
        if eval("registers['{}'] {} {}".format(cond_reg, cond_op, cond_val)):
            if op == 'inc':
                registers[reg] += val
            else:
                registers[reg] -= val

    return max(registers.values())

def solve_part_two():
    instructions = []
    for line in open('input.txt').readlines():
        reg, op, val, _, cond_reg, cond_op, cond_val = line.strip().split()
        val, cond_val = int(val), int(cond_val)
        instructions.append((reg, op, val, cond_reg, cond_op, cond_val))

    registers = defaultdict(int)
    result = 0
    for reg, op, val, cond_reg, cond_op, cond_val in instructions:
        if eval("registers['{}'] {} {}".format(cond_reg, cond_op, cond_val)):
            if op == 'inc':
                registers[reg] += val
            else:
                registers[reg] -= val
        m = max(registers.values())
        if m > result:
            result = m

    return result


def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
