def parse_input():
    rules = dict()
    for line in open("input.txt").read().splitlines():
        parts = line.split(" ")
        bag = parts[0] + " " + parts[1]
        rules[bag] = []
        i = 2
        while i < len(parts):
            if parts[i].isnumeric():
                rules[bag].append((int(parts[i]), parts[i + 1] + " " + parts[i + 2]))
            i += 1
    return rules


def can_contain(rules, bag, other):
    rule = rules[bag]
    for _, contained in rule:
        if contained == other:
            return True
        if can_contain(rules, contained, other):
            return True
    return False


def bags_needed(rules, bag):
    count = 0
    rule = rules[bag]
    for n, contained in rule:
        count += n * bags_needed(rules, contained)
    return 1 + count


def solve_part_one():
    rules = parse_input()
    count = 0
    for bag, contained in rules.items():
        if can_contain(rules, bag, "shiny gold"):
            count += 1
    return count


def solve_part_two():
    rules = parse_input()
    return bags_needed(rules, "shiny gold") - 1


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
