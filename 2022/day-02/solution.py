OUTCOMES = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

MOVES = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

MOVE_TO_PLAY = {
    ('A', 'X'): 'Z',
    ('A', 'Y'): 'X',
    ('A', 'Z'): 'Y',
    ('B', 'X'): 'X',
    ('B', 'Y'): 'Y',
    ('B', 'Z'): 'Z',
    ('C', 'X'): 'Y',
    ('C', 'Y'): 'Z',
    ('C', 'Z'): 'X',   
}

def parse_input():
    return [tuple(line.strip().split(' ')) for line in open("input.txt").readlines()]


def solve_part_one():
    return sum(OUTCOMES[x] + MOVES[x[1]] for x in parse_input())
    

def solve_part_two():
    return sum(OUTCOMES[(plays, MOVE_TO_PLAY[(plays, need_to)])] + MOVES[MOVE_TO_PLAY[(plays, need_to)]] for plays, need_to in parse_input())

def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
