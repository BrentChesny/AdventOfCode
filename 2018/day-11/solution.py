INPUT = 7400

def power_level(x, y):
    rack_id = x + 10
    power = rack_id * y
    power += INPUT
    power *= rack_id
    power = power // 100 % 10
    return power - 5

def create_cumulative_grid():
    grid = {}

    for x in range(300, 0, -1):
        for y in range(300, 0, -1):
            grid[(x, y)] = power_level(x, y) + grid.get((x + 1, y), 0) + grid.get((x, y + 1), 0) - grid.get((x + 1, y + 1), 0)

    return grid


def find_max_subgrid(size = None):
    integral_grid = create_cumulative_grid()
    max_s, max_coord, max_size = 0, None, None

    for x in range(1, 301):
        for y in range(1, 301):
            if size == None:
                sizes = range(1, 301 - max(x, y) + 1)
            else:
                sizes = [size]
            for n in sizes:
                s = integral_grid.get((x + n, y + n), 0) + integral_grid.get((x, y), 0) - integral_grid.get((x + n, y), 0) - integral_grid.get((x, y + n), 0)
                if s > max_s:
                    max_s = s
                    max_coord = (x, y)
                    max_size = n

    return max_coord, max_size

def solve_part_one():
    max_coord, _ = find_max_subgrid(3)
    return max_coord

def solve_part_two():
    coord, grid_size = find_max_subgrid()
    return coord, grid_size

def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
