def solve_part_one():
    total = 0
    a, b = generator(277, 16807), generator(349, 48271)
    for _ in range(40000000):
        x = next(a)
        y = next(b)
        if ((x ^ y) & 0xFFFF) == 0:
            total += 1
    return total

def solve_part_two():
    total = 0
    a, b = generator(277, 16807, 4), generator(349, 48271, 8)
    for _ in range(5000000):
        x = next(a)
        y = next(b)
        if ((x ^ y) & 0xFFFF) == 0:
            total += 1
    return total

def generator(seed, factor, modulus=None):
    prev = seed
    while True:
        prev *= factor
        prev %= 2147483647
        if not modulus or prev % modulus == 0:
            yield prev

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
