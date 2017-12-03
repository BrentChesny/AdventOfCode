PUZZLE_INPUT = 265149

def solve_part_one():
    ring_ends = {i: (2*i-1)**2 for i in range(1, 1000)}

    # Find relevant ring where the input is located
    for index, end_value in ring_ends.items():
        if end_value > PUZZLE_INPUT:
            ring_index, bottomright = index, end_value
            break

    # Compute other corners
    bottomleft = bottomright - 1 * (2 * (ring_index - 1))
    topleft = bottomright - 2 * (2 * (ring_index - 1))
    topright = bottomright - 3 * (2 * (ring_index - 1))

    if bottomleft <= PUZZLE_INPUT <= bottomright:
        distance = abs(((bottomleft + bottomright) / 2) - PUZZLE_INPUT)
    elif topleft <= PUZZLE_INPUT <= bottomleft:
        distance = abs(((topleft + bottomleft) / 2) - PUZZLE_INPUT)
    elif topright <= PUZZLE_INPUT <= topleft:
        distance = abs(((topright + topleft) / 2) - PUZZLE_INPUT)
    else:
        distance = abs(((ring_ends[ring_index-1] + topright) / 2) - PUZZLE_INPUT)

    return distance + (ring_index - 1)

def solve_part_two():
    grid_size = 101
    offset = (grid_size-1)/2
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    grid[offset][offset] = 1
    x = y = 0
    dx = 0
    dy = -1
    for i in range(grid_size**2):
        if (-grid_size/2 < x <= grid_size/2) and (-grid_size/2 < y <= grid_size/2):
            val = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    val += grid[offset-y+i][offset+x+j]
            grid[offset-y][offset+x] = val
            if val > PUZZLE_INPUT:
                return val
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy


def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
