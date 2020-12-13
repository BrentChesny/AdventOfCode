from functools import reduce


def parse_input():
    lines = open("input.txt").read().splitlines()
    return (
        int(lines[0]),
        [
            (idx, int(bus_id))
            for idx, bus_id in enumerate(lines[1].split(","))
            if bus_id != "x"
        ],
    )


def solve_part_one():
    start_time, bus_ids = parse_input()
    time = start_time
    while True:
        for _, bus_id in bus_ids:
            if time % bus_id == 0:
                return (time - start_time) * bus_id
        time += 1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# This problem boils down to solving a set of congruences.
# The chinese remainder theorem can be used to solve this.
def solve_part_two():
    _, bus_ids = parse_input()
    a = [-idx for idx, _ in bus_ids]
    n = [bus_id for _, bus_id in bus_ids]
    return chinese_remainder(n, a)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
