def parse_input():
    return [(line[0], int(line[1:])) for line in open("input.txt").read().splitlines()]


def turn_left(x, y):
    return -y, x


def turn_right(x, y):
    return y, -x


def solve_part_one():
    x, y = 0, 0
    d = (1, 0)
    for instr, val in parse_input():
        if instr == "N":
            y += val
        elif instr == "E":
            x += val
        elif instr == "S":
            y -= val
        elif instr == "W":
            x -= val
        elif instr == "L":
            turns = val // 90
            for _ in range(turns):
                d = turn_left(*d)
        elif instr == "R":
            turns = val // 90
            for _ in range(turns):
                d = turn_right(*d)
        elif instr == "F":
            x += val * d[0]
            y += val * d[1]
    return abs(x) + abs(y)


def solve_part_two():
    wx, wy = 10, 1
    x, y = 0, 0
    for instr, val in parse_input():
        if instr == "N":
            wy += val
        elif instr == "E":
            wx += val
        elif instr == "S":
            wy -= val
        elif instr == "W":
            wx -= val
        elif instr == "L":
            turns = val // 90
            for _ in range(turns):
                wx, wy = turn_left(wx, wy)
        elif instr == "R":
            turns = val // 90
            for _ in range(turns):
                wx, wy = turn_right(wx, wy)
        elif instr == "F":
            x += val * wx
            y += val * wy
    return abs(x) + abs(y)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
