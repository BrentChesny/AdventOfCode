def solve_part_one():
    digits = map(int, list(open('input.txt').read().strip()))
    n = len(digits)
    total = 0

    for i in range(len(digits)):
        total += digits[i] if digits[i] == digits[(i+1) % n] else 0

    return total


def solve_part_two():
    digits = map(int, list(open('input.txt').read().strip()))
    n = len(digits)
    total = 0

    for i in range(len(digits)):
        total += digits[i] if digits[i] == digits[(i + (n/2)) % n] else 0

    return total

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
