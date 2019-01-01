def parse_input():
    return [tuple(map(int, line.strip().split(','))) for line in open('input.txt').readlines()]

def dist(p1, p2):
    x1, y1, z1, t1 = p1
    x2, y2, z2, t2 = p2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) + abs(t1 - t2)

def solve_part_one():
    points = parse_input()

    constellations = []
    current = set()

    while points:
        while True:
            i = 0
            while i < len(points):
                found = False
                point = points[i]
                if not current:
                    current.add(point)
                    points.pop(i)
                    found = True
                    break
                for p in current:
                    d = dist(point, p)
                    if d <= 3:
                        current.add(point)
                        points.pop(i)
                        found = True
                        break
                if found:
                    break
                else:
                    i += 1
            if i == len(points):
                break
        constellations.append(current)
        current = set()

    return len(constellations)


def main():
    print('Part one: ', solve_part_one())


if __name__ == '__main__':
    main()
