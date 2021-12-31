from itertools import cycle, product
from functools import lru_cache


def parse_input():
    lines = [line.strip().split(" ") for line in open("input.txt")]
    return [int(lines[0][-1]), int(lines[1][-1])]


def rollover(n, limit):
    while n > limit:
        n -= limit
    return n


def deterministic_die():
    val = 1
    while True:
        yield val
        val += 1
        val = rollover(val, 100)


def dirac_die():
    val = 1
    while True:
        yield val
        val += 1
        val = rollover(val, 100)


def solve_part_one():
    scores = [0, 0]
    pos = parse_input()
    rolls = 0
    die = deterministic_die()
    for p in cycle([0, 1]):
        r1 = next(die)
        r2 = next(die)
        r3 = next(die)
        roll = r1 + r2 + r3
        rolls += 3
        pos[p] += roll
        pos[p] = rollover(pos[p], 10)
        scores[p] += pos[p]
        if scores[p] >= 1000:
            return scores[p - 1] * rolls


@lru_cache(maxsize=None)
def play_dirac(p1, p2, s1, s2):
    w1, w2 = 0, 0
    for r1, r2, r3 in product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        roll = r1 + r2 + r3
        p1_new = rollover(p1 + roll, 10)
        s1_new = s1 + p1_new
        if s1_new >= 21:
            w1 += 1
        else:
            wins2, wins1 = play_dirac(p2, p1_new, s2, s1_new)
            w1 += wins1
            w2 += wins2
    return w1, w2


def solve_part_two():
    p1, p2 = parse_input()
    return max(play_dirac(p1, p2, 0, 0))


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
