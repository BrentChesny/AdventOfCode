from os import supports_bytes_environ
import re


def parse_input():
    content = open("input.txt").read()
    rules, messages = content.split("\n\n")
    parsed_rules = dict()
    for line in rules.splitlines():
        idx, rule = line.split(": ")
        if not '"' in rule:
            rule = "(" + rule + ")"
        else:
            rule = rule.replace('"', "")
        parsed_rules[idx] = rule
    return parsed_rules, messages.splitlines()


def construct_regex(rule, rules):
    subs = set(re.findall(r"\d+", rule))

    # Make sure we do al substitutions from high to low index to prevent wrong substitutions
    subs = map(int, subs)
    subs = sorted(subs, reverse=True)
    subs = map(str, subs)

    for sub in subs:
        rule = rule.replace(sub, construct_regex(rules[sub], rules))

    rule = rule.replace(" ", "")
    return rule


def solve_part_one():
    rules, messages = parse_input()

    regex = re.compile("^" + construct_regex(rules["0"], rules) + "$")

    return sum(1 for message in messages if regex.match(message))


def solve_part_two():
    rules, messages = parse_input()

    # Make the adjustments for part two, without introducing infinite recursion ;)
    # Here we make use of the fact that the rules use a simple recursion on the same rule.
    rules["8"] = "(42)+"
    for i in range(2, 10):
        rules["11"] += " | " + " ".join(["42"] * i + ["31"] * i)
    rules["11"] = "(" + rules["11"] + ")"

    regex = re.compile("^" + construct_regex(rules["0"], rules) + "$")

    return sum(1 for message in messages if regex.match(message))


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
