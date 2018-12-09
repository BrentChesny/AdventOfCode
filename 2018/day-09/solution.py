import re
from collections import defaultdict, deque

def parse_input():
    return tuple(map(int, re.findall(r'\d+', open('input.txt').read())))

def play(n_players, n_marbles):
    circle = deque([0])
    current_player = 0
    scores = defaultdict(int)

    for marble in range(1, n_marbles + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[current_player] += marble + circle.popleft()
        else:
            circle.rotate(-2)
            circle.appendleft(marble)

        current_player = (current_player + 1) % n_players

    return max(scores.values())

def solve_part_one():
    n_players, n_marbles = parse_input()
    return play(n_players, n_marbles)


def solve_part_two():
    n_players, n_marbles = parse_input()
    return play(n_players, n_marbles * 100)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
