def solve_part_one():
    def gen_a():
        prev = 277
        while True:
            prev *= 16807
            prev %= 2147483647
            yield prev

    def gen_b():
        prev = 349
        while True:
            prev *= 48271
            prev %= 2147483647
            yield prev

    total = 0
    a, b = gen_a(), gen_b()
    for _ in range(40000000):
        x = next(a)
        y = next(b)
        if ((x ^ y) & 0xFFFF) == 0:
            total += 1
    return total

def solve_part_two():
    def gen_a():
        prev = 277
        while True:
            prev *= 16807
            prev %= 2147483647
            if prev % 4 == 0:
                yield prev

    def gen_b():
        prev = 349
        while True:
            prev *= 48271
            prev %= 2147483647
            if prev % 8 == 0:
                yield prev

    total = 0
    a, b = gen_a(), gen_b()
    for _ in range(5000000):
        x = next(a)
        y = next(b)
        if ((x ^ y) & 0xFFFF) == 0:
            total += 1
    return total

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
