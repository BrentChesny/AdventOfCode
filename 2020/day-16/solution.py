from collections import defaultdict


def parse_input():
    rules = defaultdict(set)
    tickets = []
    for line in open("input.txt").read().splitlines():
        if "ticket" in line:
            continue
        elif ":" in line:
            field, values = line.split(":")
            ranges = values.split("or")
            for r in ranges:
                f, t = map(int, r.split("-"))
                rules[field].update(range(f, t + 1))
        elif "," in line:
            tickets.append(list(map(int, line.split(","))))
    return rules, tickets[0], tickets[1:]


def solve_part_one():
    rules, my_ticket, other_tickets = parse_input()

    all_valid_values = set.union(*rules.values())
    all_invalid_values = []
    for t in other_tickets:
        all_invalid_values.extend(set(t).difference(all_valid_values))

    return sum(all_invalid_values)


def solve_part_two():
    rules, my_ticket, other_tickets = parse_input()

    all_valid_values = set.union(*rules.values())
    all_invalid_values = []
    valid_tickets = [t for t in other_tickets if set(t).issubset(all_valid_values)]

    values = [{t[i] for t in valid_tickets} for i in range(len(rules))]

    assignment = [
        {
            field
            for field, valid_values in rules.items()
            if values[i].issubset(valid_values)
        }
        for i in range(len(rules))
    ]

    changed = True
    decided = []
    while changed:
        changed = False
        new_decided = {list(f)[0] for f in assignment if len(f) == 1}
        if len(new_decided) > len(decided):
            changed = True
        assignment = [
            f if len(f) == 1 else f.difference(new_decided) for f in assignment
        ]
        decided = new_decided

    assignment = [list(f)[0] for f in assignment]

    result = 1
    for i, field in enumerate(assignment):
        if "departure" in field:
            result *= my_ticket[i]
    return result


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
