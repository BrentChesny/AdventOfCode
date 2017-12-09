def solve_part_one():
    puzzle = open('input.txt').read()

    depth = 0
    result = 0
    in_garbage = False
    ignore_character = False

    for c in puzzle:
        if c == '!' and not ignore_character:
            ignore_character = True
        elif ignore_character:
            ignore_character = False
            continue
        elif c == '<':
            in_garbage = True
        elif c == '>':
            in_garbage = False
        elif in_garbage:
            continue
        elif c == '{':
            depth += 1
        elif c == '}':
            result += depth
            depth -= 1

    return result

def solve_part_two():
    puzzle = open('input.txt').read()

    result = 0
    in_garbage = False
    ignore_character = False

    for c in puzzle:
        if in_garbage:
            result += 1
        if c == '!' and not ignore_character:
            ignore_character = True
            result -= 1
        elif ignore_character:
            ignore_character = False
            result -= 1
            continue
        elif c == '<':
            in_garbage = True
        elif c == '>':
            in_garbage = False
            result -= 1
        elif in_garbage:
            continue

    return result


def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
