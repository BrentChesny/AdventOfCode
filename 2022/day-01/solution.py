def parse_input():
    result = []
    current = []
    for line in open("input.txt").readlines():
        if line.strip() == "":
            result.append(current)
            current = []
        else:
            current.append(int(line.strip()))
    result.append(current)
    return result


def solve_part_one():
    calories = parse_input()
    return max(sum(x) for x in calories)
    


def solve_part_two():
    calories = parse_input()
    return sum(sorted(sum(x) for x in calories)[-3:])


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
