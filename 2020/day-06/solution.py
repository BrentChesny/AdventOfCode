def parse_input():
    body = open("input.txt").read()
    groups = body.split("\n\n")
    return [[set(p) for p in g.split("\n")] for g in groups]


def solve_part_one():
    return sum(len(set.union(*g)) for g in parse_input())


def solve_part_two():
    return sum(len(set.intersection(*g)) for g in parse_input())


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
