from collections import defaultdict


def parse_input():
    return [int(line) for line in open("input.txt").readline().strip().split(",")]


def to_counts(ages):
    fish = defaultdict(int)
    for age in ages:
        fish[age] += 1
    return fish


def live_a_day(fish):
    new_fish = fish.count(0)
    return (
        list(map(lambda age: (age - 1) % 7 if age < 7 else age - 1, fish))
        + [8] * new_fish
    )


def live_seven_days(fish):
    new_fish = defaultdict(int)
    for age, count in fish.items():
        new_fish[age % 7] += count
    for age in range(7):
        new_fish[age + 2] += fish[age]
    return new_fish


# 0 -> 2
# 1 -> 3
# 2    4
# 3    5
# 4    6
# 5    7
# 6    8


def solve_part_one():
    ages = parse_input()
    for _ in range(3):
        ages = live_a_day(ages)
    counts = to_counts(ages)
    for _ in range(11):
        counts = live_seven_days(counts)
    return sum(c for c in counts.values())


def solve_part_two():
    ages = parse_input()
    for _ in range(4):
        ages = live_a_day(ages)
    counts = to_counts(ages)
    for _ in range(36):
        counts = live_seven_days(counts)
    return sum(c for c in counts.values())


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
