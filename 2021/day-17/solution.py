import re

regex = re.compile("target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)")


def parse_input():
    target = open("input.txt").read().strip()
    minx, maxx, miny, maxy = regex.match(target).groups()
    return int(minx), int(maxx), int(miny), int(maxy)


def in_target(x, y, target):
    minx, maxx, miny, maxy = target
    return minx <= x <= maxx and miny <= y <= maxy


def simulate(vx, vy, target):
    px, py = 0, 0
    max_y = 0
    while py > -1000:
        px += vx
        py += vy
        if vx != 0:
            vx += 1 if vx < 0 else -1
        vy -= 1
        max_y = max(max_y, py)
        if in_target(px, py, target):
            return True, max_y
    return False, max_y


def solve_part_one():
    target = parse_input()
    max_ys = []
    for vx in range(0, 200):
        for vy in range(0, 200):
            reached, max_y = simulate(vx, vy, target)
            if reached:
                max_ys.append(max_y)
    return max(max_ys)


def solve_part_two():
    target = parse_input()
    possible_vs = set()
    for vx in range(0, 500):
        for vy in range(-500, 500):
            reached, _ = simulate(vx, vy, target)
            if reached:
                possible_vs.add((vx, vy))
    return len(possible_vs)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
