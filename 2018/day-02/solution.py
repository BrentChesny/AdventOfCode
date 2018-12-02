from collections import Counter, defaultdict

def parse_input():
    return open('input.txt').read().strip().split('\n')

def solve_part_one():
    similar = defaultdict(int)
    for box in parse_input():
        for x in set(Counter(box).values()):
            similar[x] += 1
    return similar[2] * similar[3]

def solve_part_two():
    boxes = parse_input()
    for first in boxes:
        for second in boxes:
            result = [x for x, y in zip(first, second) if x == y]
            if len(result) == len(first) - 1:
                return ''.join(result)

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
