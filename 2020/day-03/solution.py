def parse_input():
    return [line.strip() for line in open("input.txt")]


def count_trees_for_slope(grid, down, right):
    r, c, count = 0, 0, 0
    while r < len(grid):
        if grid[r][c % len(grid[0])] == "#":
            count += 1
        r, c = r + down, c + right
    return count


def solve_part_one():
    grid = parse_input()
    return count_trees_for_slope(grid, 1, 3)


def solve_part_two():
    grid = parse_input()
    return (
        count_trees_for_slope(grid, 1, 1)
        * count_trees_for_slope(grid, 1, 3)
        * count_trees_for_slope(grid, 1, 5)
        * count_trees_for_slope(grid, 1, 7)
        * count_trees_for_slope(grid, 2, 1)
    )


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
