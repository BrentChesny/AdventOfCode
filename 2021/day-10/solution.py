OPENINGS = ["(", "[", "{", "<"]
CLOSINGS = [")", "]", "}", ">"]

CORRUPTION_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

COMPLETION_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def parse_input():
    return [line.strip() for line in open("input.txt")]


def matches(opening, closing):
    i = OPENINGS.index(opening)
    return closing == CLOSINGS[i]


def get_correct_closing(opening):
    i = OPENINGS.index(opening)
    return CLOSINGS[i]


def completion_score(stack):
    score = 0
    for opening in reversed(stack):
        score = score * 5 + COMPLETION_SCORES[get_correct_closing(opening)]
    return score


def check_line(line):
    stack = []
    for c in line:
        if c in OPENINGS:
            stack.append(c)
        else:
            p = stack.pop()
            if not matches(p, c):
                return "corrupted", CORRUPTION_SCORES[c]
    if stack:
        return "incomplete", completion_score(stack)
    return "ok", None


def solve_part_one():
    score = 0
    for line in parse_input():
        status, result = check_line(line)
        if status == "corrupted":
            score += result
    return score


def solve_part_two():
    scores = []
    for line in parse_input():
        status, result = check_line(line)
        if status == "incomplete":
            scores.append(result)
    return sorted(scores)[len(scores) // 2]


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
