from functools import cache


def parse_input():
    return [int(line) for line in open("input.txt").readline().strip().split(",")]


def calculate_fuel(crabs, target):
    return sum(abs(target - crab) for crab in crabs)


@cache
def fuel_for_distance(distance):
    return sum(range(1, distance + 1))


def calculate_fuel_correctly(crabs, target):
    return sum(fuel_for_distance(abs(target - crab)) for crab in crabs)


def solve_part_one():
    crabs = parse_input()
    mn = min(crabs)
    mx = max(crabs)
    return min(calculate_fuel(crabs, target) for target in range(mn, mx + 1))


def solve_part_two():
    crabs = parse_input()
    mn = min(crabs)
    mx = max(crabs)
    return min(calculate_fuel_correctly(crabs, target) for target in range(mn, mx + 1))


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
