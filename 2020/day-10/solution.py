def parse_input():
    return [int(line) for line in open("input.txt")]


def solve_part_one():
    adapters = sorted(parse_input())
    jolts = [0] + adapters + [max(adapters) + 3]
    differences = [b - a for a, b in zip(jolts, jolts[1:])]
    return differences.count(1) * differences.count(3)


def solve_part_two():
    adapters = sorted(parse_input())
    m = max(adapters)
    dp = [1] + [0] * (m)
    for a in adapters:
        dp[a] = dp[a - 1] + dp[a - 2] + dp[a - 3]
    return dp


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
