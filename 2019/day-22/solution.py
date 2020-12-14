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
        i = (i + n) % l

    return new_stack


def parse_input():
    process = []
    for line in open("input.txt").readlines():
        parts = line.strip().split(" ")
        if parts[0] == "cut":
            process.append((parts[0], cut_n, int(parts[1])))
        elif parts[1] == "into":
            process.append((parts[1], deal_new_stack, 0))
        elif parts[1] == "with":
            process.append((parts[1], deal_with_incr, int(parts[3])))
    return process


def solve_part_one():
    process = parse_input()
    stack = list(range(10007))

    for _, technique, n in process:
        stack = technique(stack, n)

    return stack.index(2019)


def solve_part_two():
    process = parse_input()
    n_shuffles = 101741582076661
    mod = 119315717514047

    offset, increment = 0, 1

    # Calculate offset and increment change in one shuffle pass
    for technique, _, n in process:
        if technique == "cut":
            offset += increment * n
        elif technique == "into":
            increment *= -1
            offset += increment
        elif technique == "with":
            increment *= inv(n, mod)

    offset_diff = offset % mod
    increment_mul = increment % mod

    increment = pow(increment_mul, n_shuffles, mod)
    offset = (
        offset_diff
        * (1 - pow(increment_mul, n_shuffles, mod))
        * inv(1 - increment_mul, mod)
    )

    return (offset + increment * 2020) % mod


# Calculates the modular multiplicative inverse (using fermat's little theorem)
def inv(n, mod):
    return pow(n, mod - 2, mod)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
