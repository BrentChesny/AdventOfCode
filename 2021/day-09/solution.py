def parse_input():
    return [[int(x) for x in line.strip()] for line in open("input.txt")]


def neighbors(r, c, heights):
    return [
        (r + dr, c + dc, heights[r + dr][c + dc])
        for dr in range(-1, 2)
        for dc in range(-1, 2)
        if 0 <= r + dr < len(heights)
        and 0 <= c + dc < len(heights[0])
        and (dr != 0 or dc != 0)
        and (dr == 0 or dc == 0)
    ]


def find_low_points(heights):
    lows = []
    for r in range(len(heights)):
        for c in range(len(heights[0])):
            v = heights[r][c]
            if all(v < n for _, _, n in neighbors(r, c, heights)):
                lows.append((r, c))
    return lows


def solve_part_one():
    heights = parse_input()
    result = 0
    for r, c in find_low_points(heights):
        result += heights[r][c] + 1
    return result


def discover_bassin(low, heights):
    r, c = low
    bassin = set([(r, c, heights[r][c])])
    while True:
        to_add = set()
        for r, c, h in bassin:
            for rr, cc, n in neighbors(r, c, heights):
                if h <= n < 9 and (rr, cc, n) not in bassin:
                    to_add.add((rr, cc, n))
        if len(to_add) > 0:
            bassin |= to_add
        else:
            return bassin


def solve_part_two():
    heights = parse_input()
    lows = find_low_points(heights)
    bassin_sizes = sorted(
        [len(discover_bassin(low, heights)) for low in find_low_points(heights)],
        reverse=True,
    )
    return bassin_sizes[0] * bassin_sizes[1] * bassin_sizes[2]


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
