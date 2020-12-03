def deal_new_stack(stack, _):
    return list(reversed(stack))


def cut_n(stack, n):
    return stack[n:] + stack[:n]


def deal_with_incr(stack, n):
    l = len(stack)
    new_stack = [None for _ in range(l)]

    i = 0
    while stack:
        new_stack[i] = stack.pop(0)
        i = (i+n) % l

    return new_stack


def parse_input():
    process = []
    for line in open('input.txt').readlines():
        parts = line.strip().split(' ')
        if parts[0] == 'cut':
            process.append((cut_n, int(parts[1])))
        elif parts[1] == 'into':
            process.append((deal_new_stack, 0))
        elif parts[1] == 'with':
            process.append((deal_with_incr, int(parts[3])))
    return process


def solve_part_one():
    process = parse_input()
    stack = list(range(10007))

    for technique, n in process:
        stack = technique(stack, n)

    return stack.index(2019)


def solve_part_two():
    process = parse_input()
    stack = list(range(10))

    for technique, n in process:
        stack = technique(stack, n)

    return stack


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
