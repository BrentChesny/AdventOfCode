TARGET_VALUE = 19690720

def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))

def execute(program):
    ip = 0

    while program[ip] != 99:
        instruction = program[ip]
        if instruction == 1:
            program[program[ip+3]] = program[program[ip+1]] + program[program[ip+2]]
        elif instruction == 2:
            program[program[ip+3]] = program[program[ip+1]] * program[program[ip+2]]
        ip += 4

def solve_part_one():
    program = parse_input()
    program[1] = 12
    program[2] = 2
    execute(program)
    return program[0]

def solve_part_two():
    program = parse_input()

    for noun in range(100):
        for verb in range(100):
            running_program = program[:]
            running_program[1] = noun
            running_program[2] = verb
            execute(running_program)
            if running_program[0] == TARGET_VALUE:
                return noun * 100 + verb


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())

if __name__ == '__main__':
    main()
