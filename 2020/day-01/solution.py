def parse_input():
    return [int(line) for line in open("input.txt").readlines()]


def solve_part_one():
    expenses = parse_input()
    return [x * y for x in expenses for y in expenses if x + y == 2020][0]


def solve_part_two():
    expenses = parse_input()
    return [
        x * y * z
        for x in expenses
        for y in expenses
        for z in expenses
        if x + y + z == 2020
    ][0]


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
