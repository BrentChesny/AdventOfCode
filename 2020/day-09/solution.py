def parse_input():
    return [int(line) for line in open("input.txt")]


def solve_part_one():
    data = parse_input()
    for idx in range(25, len(data)):
        n = data[idx]
        valid = False
        for x in data[idx - 25 : idx]:
            for y in data[idx - 25 : idx]:
                if x != y and x + y == n:
                    valid = True
        if not valid:
            return n


def solve_part_two():
    data = parse_input()
    invalid = solve_part_one()
    for start in range(len(data)):
        for end in range(start, len(data)):
            section = data[start : end + 1]
            if sum(section) == invalid:
                return min(section) + max(section)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
