from itertools import cycle


def parse_input():
    return list(map(int, '12345678910111213'))
    return list(map(int, open('input.txt').read().strip()))


def get_pattern(i):
    n = i + 1
    return [0] * n + [1] * n + [0] * n + [-1] * n


def execute_phase(signal):
    result = []

    for i in range(len(signal)):
        pattern = cycle(get_pattern(i))
        next(pattern)
        value = abs(sum(a*b for a, b in zip(signal, pattern))) % 10
        result.append(value)

    return result


def solve_part_one():
    signal = parse_input()
    for idx in range(100):
        print(signal, idx)
        signal = execute_phase(signal)
    return ''.join(map(str, signal[:8]))


def solve_part_two():
    pass


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
