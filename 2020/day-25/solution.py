from typing import ClassVar


def parse_input():
    return list(map(int, open("input.txt").read().splitlines()))


def determine_loop_size(key):
    v = 1
    subject = 7
    i = 1
    while True:
        v *= subject
        v %= 20201227
        if v == key:
            return i
        i += 1


def transform(subject, loop_size):
    v = 1
    for _ in range(loop_size):
        v *= subject
        v %= 20201227
    return v


def solve_part_one():
    door_key, card_key = parse_input()
    card_loop_size = determine_loop_size(card_key)
    return transform(door_key, card_loop_size)


def main():
    print("Part one: ", solve_part_one())


if __name__ == "__main__":
    main()
