from itertools import cycle

def parse_input():
    return [int(line) for line in open('input.txt').readlines()]

def solve_part_one():
    return sum(parse_input())

def solve_part_two():
    current_freq, seen = 0, {0}
    for delta in cycle(parse_input()):
        current_freq += delta
        if current_freq in seen:
            return current_freq
        seen.add(current_freq)


def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
