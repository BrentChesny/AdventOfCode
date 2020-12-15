from collections import defaultdict


def parse_input():
    return list(map(int, "1,12,0,20,8,16".split(",")))


def nth_number(n):
    turn = 1
    last_spoken = defaultdict(list)
    previous_spoken = None

    for starting_number in parse_input():
        previous_spoken = starting_number
        last_spoken[starting_number].append(turn)
        turn += 1

    while True:
        a = last_spoken[previous_spoken]
        if len(a) > 1:
            b = a[-1] - a[-2]
        else:
            b = 0
        if turn == n:
            return b
        previous_spoken = b
        last_spoken[b].append(turn)
        turn += 1


def solve_part_one():
    return nth_number(2020)


def solve_part_two():
    return nth_number(30000000)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
