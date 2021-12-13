import re

regex = re.compile("fold along ([xy])=(\d+)")


def parse_input():
    lines = open("input.txt").read()
    points, folds = lines.split("\n\n")
    points = [tuple(map(int, line.split(","))) for line in points.split("\n")]
    folds = [regex.match(line).groups() for line in folds.split("\n")]
    folds = [(0 if d == "x" else 1, int(c)) for d, c in folds]
    return set(points), folds


def fold(points, d, coord):
    folded_points = set()
    for point in points:
        if point[d] < coord:
            folded_points.add(point)
        else:
            folded = None
            if d == 0:
                folded = (coord - abs(point[0] - coord), point[1])
            else:
                folded = (point[0], coord - abs(point[1] - coord))
            folded_points.add(folded)
    return folded_points


def solve_part_one():
    points, folds = parse_input()
    d, coord = folds[0]
    return len(fold(points, d, coord))


def draw(points):
    min_x = min(x for x, y in points)
    min_y = min(y for x, y in points)
    max_x = max(x for x, y in points)
    max_y = max(y for x, y in points)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                tile = "X"
            else:
                tile = " "
            print(tile, end="")
        print()


def solve_part_two():
    points, folds = parse_input()
    for d, coord in folds:
        points = fold(points, d, coord)
    draw(points)
    return "See drawing"


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
