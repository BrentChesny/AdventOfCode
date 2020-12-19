from collections import OrderedDict


def parse_input():
    return [line for line in open("input.txt").read().splitlines()]


ops = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
}


def precedes(precedences, op1, op2):
    return precedences[op1] >= precedences[op2]


def evaluate(expr, precedences):
    value_stack = []
    op_stack = []

    for c in expr:
        if c == " ":
            continue
        if c.isnumeric():
            value_stack.append(int(c))
        if c == "(":
            op_stack.append(c)
        if c == ")":
            while op_stack[-1] != "(":
                op = op_stack.pop()
                a = value_stack.pop()
                b = value_stack.pop()
                value_stack.append(ops[op](a, b))
            op_stack.pop()
        if c in ["+", "*"]:
            while op_stack and precedes(precedences, op_stack[-1], c):
                op = op_stack.pop()
                a = value_stack.pop()
                b = value_stack.pop()
                value_stack.append(ops[op](a, b))
            op_stack.append(c)

    while op_stack:
        op = op_stack.pop()
        a = value_stack.pop()
        b = value_stack.pop()
        value_stack.append(ops[op](a, b))

    assert len(op_stack) == 0
    assert len(value_stack) == 1

    return value_stack[0]


def solve_part_one():
    precedences = {"(": 0, ")": 0, "*": 1, "+": 1}
    expressions = parse_input()
    return sum(evaluate(expr, precedences) for expr in expressions)


def solve_part_two():
    precedences = {"(": 0, ")": 0, "*": 1, "+": 2}
    expressions = parse_input()
    return sum(evaluate(expr, precedences) for expr in expressions)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
