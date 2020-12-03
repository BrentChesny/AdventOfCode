import re

regex = re.compile("(\d+)-(\d+) (\w): (\w+)")


def parse_input():
    result = []
    for line in open("input.txt"):
        mn, mx, ch, pw = regex.match(line).groups()
        result.append((int(mn), int(mx), ch, pw))
    return result


def count_char(ch, str):
    return len([c for c in str if c == ch])


def solve_part_one():
    return len(
        [pw for mn, mx, ch, pw in parse_input() if mn <= count_char(ch, pw) <= mx]
    )


def solve_part_two():
    return len(
        [
            pw
            for mn, mx, ch, pw in parse_input()
            if (pw[mn - 1] == ch or pw[mx - 1] == ch) and pw[mn - 1] != pw[mx - 1]
        ]
    )


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
