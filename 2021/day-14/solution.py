from collections import Counter, defaultdict


def parse_input():
    lines = [line.strip() for line in open("input.txt")]
    template = lines[0]
    rules = {x: y for x, y in [line.split(" -> ") for line in lines[2:]]}
    return template, rules


def step(template, rules):
    inserted = ""
    for a, b in zip(template, template[1:]):
        inserted += a
        if a + b in rules:
            inserted += rules[a + b]
    inserted += template[-1]
    return inserted


def solve_part_one():
    template, rules = parse_input()
    for _ in range(10):
        template = step(template, rules)
    c = Counter(template).most_common()
    return c[0][1] - c[-1][1]


def step_smart(template, doubles, rules):
    inserted = defaultdict(int)
    for pair, c in template.items():
        if pair in rules:
            insertion = rules[pair]
            inserted[pair[0] + insertion] += c
            inserted[insertion + pair[1]] += c
            doubles[insertion] += c
    return inserted, doubles


def count(ch, template):
    return sum(pair.count(ch) * c for pair, c in template.items() if ch in pair)


def solve_part_two():
    template, rules = parse_input()
    doubles = defaultdict(int)
    doubles.update(Counter(template[1:-1]))
    template = {a + b: 1 for a, b in zip(template, template[1:])}
    for _ in range(40):
        template, doubles = step_smart(template, doubles, rules)
    chars = [ch for pair in template for ch in pair]
    counts = [count(ch, template) - doubles[ch] for ch in chars]
    counts = sorted(counts)
    return counts[-1] - counts[0]


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
