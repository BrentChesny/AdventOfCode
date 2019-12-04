INPUT = '124075-580769'


double_digits = {i: str(i)*2 for i in range(10)}
more_digits = {i: [str(i)*n for n in range(3, 7)] for i in range(10)}


def parse_input():
    start, end = map(int, INPUT.split('-'))
    return map(str, range(start, end+1))


def has_double_digit(password):
    return any(substr in password for digit, substr in double_digits.items())


def has_double_digit_but_not_more(password):
    return any(substr in password and all(s not in password for s in more_digits[digit]) for digit, substr in double_digits.items())


def is_increasing(password):
    last_digit = 0
    for digit in map(int, password):
        if digit < last_digit:
            return False
        last_digit = digit
    return True


def solve_part_one():
    return sum(1 for pw in parse_input() if has_double_digit(pw) and is_increasing(pw))


def solve_part_two():
    return sum(1 for pw in parse_input() if has_double_digit_but_not_more(pw) and is_increasing(pw))


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
