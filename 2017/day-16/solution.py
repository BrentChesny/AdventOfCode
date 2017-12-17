def parse_input():
    dance = open('input.txt').read().strip().split(',')
    return dance

def solve_part_one():
    dance = parse_input()
    programs = [chr(ord('a') + i) for i in range(16)]

    return ''.join(perform_dance(programs, dance))

def solve_part_two():
    dance = parse_input()
    programs = [chr(ord('a') + i) for i in range(16)]

    seen = []
    for i in range(1000000000):
        if ''.join(programs) in seen:
            return seen[1000000000 % i]
        seen.append(''.join(programs))

        programs = perform_dance(programs, dance)

def perform_dance(programs, dance):
    for move in dance:
        if move[0] == 's':
            steps = int(move[1:])
            programs = programs[-steps:] + programs[:-steps]
        elif move[0] == 'x':
            i1, i2 = map(int, move[1:].split('/'))
            programs[i1], programs[i2] = programs[i2], programs[i1]
        elif move[0] == 'p':
            i1, i2 = map(lambda p: programs.index(p), move[1:].split('/'))
            programs[i1], programs[i2] = programs[i2], programs[i1]
    return programs

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
