def solve_part_one():
    instructions = map(int, open('input.txt').readlines())
    pc, result = 0, 0

    while pc < len(instructions):
        jump = instructions[pc]
        instructions[pc] += 1
        pc += jump
        result += 1

    return result

def solve_part_two():
    instructions = map(int, open('input.txt').readlines())
    pc, result = 0, 0

    while pc < len(instructions):
        jump = instructions[pc]
        if instructions[pc] < 3:
            instructions[pc] += 1
        else:
            instructions[pc] -= 1
        pc += jump
        result += 1

    return result

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
