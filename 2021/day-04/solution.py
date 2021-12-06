BOARD_SIZE = 5


def parse_input():
    lines = [line.strip() for line in open("input.txt").readlines()]
    numbers, lines = map(int, lines[0].split(",")), lines[1:]
    raw_boards = [
        [
            [
                int(n)
                for n in line.split(
                    " ",
                )
                if n != ""
            ]
            for line in lines[i + 1 : i + BOARD_SIZE + 1]
        ]
        for i in range(0, len(lines), BOARD_SIZE + 1)
    ]
    boards = []
    for board in raw_boards:
        rows = [set(line) for line in board]
        cols = [set(line) for line in zip(*board)]
        boards.append((rows, cols))
    return numbers, boards


def is_solved(board, drawn):
    rows, cols = board
    for row in rows:
        if row.issubset(drawn):
            return True
    for col in cols:
        if col.issubset(drawn):
            return True
    return False


def unmarked_sum(board, drawn):
    rows, _ = board
    score = 0
    for row in rows:
        for n in row:
            if n not in drawn:
                score += n
    return score


def solve_part_one():
    numbers, boards = parse_input()
    drawn = set()
    for n in numbers:
        drawn.add(n)
        for board in boards:
            if is_solved(board, drawn):
                return unmarked_sum(board, drawn) * n


def solve_part_two():
    numbers, boards = parse_input()
    drawn = set()
    won_boards = set()
    for n in numbers:
        drawn.add(n)
        for i, board in enumerate(boards):
            if is_solved(board, drawn):
                won_boards.add(i)
            if len(won_boards) == len(boards):
                return unmarked_sum(board, drawn) * n


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
