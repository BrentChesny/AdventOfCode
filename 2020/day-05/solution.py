def parse_input():
    return [line.strip() for line in open("input.txt").readlines()]


def convert(partitioning):
    p = len(partitioning) - 1
    seat = 0
    for c in partitioning:
        if c in ["B", "R"]:
            seat += 2 ** p
        p -= 1
    return seat


def solve_part_one():
    return max(convert(bp[:7]) * 8 + convert(bp[-3:]) for bp in parse_input())


def solve_part_two():
    seats = {convert(bp[:7]) * 8 + convert(bp[-3:]) for bp in parse_input()}
    for s in range(1, 10001):
        if s not in seats and s - 1 in seats and s + 1 in seats:
            return s


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
