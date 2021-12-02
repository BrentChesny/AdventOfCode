def parse_input():
    return [int(line) for line in open("input.txt").readlines()]


def solve_part_one():
    depths = parse_input()
    count = 0
    for a, b in zip(depths, depths[1:]):
        if b > a:
            count += 1
    return count


def solve_part_two():
    depths = parse_input()
    windows = [x + y + z for x, y, z in zip(depths, depths[1:], depths[2:])]
    count = 0
    for a, b in zip(windows, windows[1:]):
        if b > a:
            count += 1
    return count


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
