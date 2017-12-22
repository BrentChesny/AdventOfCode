from collections import defaultdict

CLEAN = 0
FLAGGED = 1
INFECTED = 2
WEAKENED = 3

DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

def parse_input():
    grid = [line.strip() for line in open('input.txt').readlines()]
    h = len(grid)
    w = len(grid[0])
    grid_dict = defaultdict(int)
    for i in xrange(h):
        for j in xrange(w):
            grid_dict[(i-h/2, j-w/2)] = INFECTED if grid[i][j] == '#' else CLEAN
    return grid_dict

def solve_part_one():
    grid = parse_input()
    pos = (0, 0)
    direction = 0
    result = 0

    for _ in xrange(10000):
    	if grid[pos] == INFECTED:
    		direction = (direction + 1) % 4
    	else:
    		direction = (direction - 1) % 4
    	grid[pos] = INFECTED if grid[pos] == CLEAN else CLEAN
        if grid[pos] == INFECTED:
            result += 1
        dr, dc = DIRECTIONS[direction]
    	pos = (pos[0] + dr, pos[1] + dc)

    return result

def solve_part_two():
    grid = parse_input()
    pos = (0, 0)
    direction = 0
    result = 0

    for _ in xrange(10000000):
    	if grid[pos] == INFECTED:
    		direction = (direction + 1) % 4
        elif grid[pos] == FLAGGED:
            direction = (direction + 2) % 4
    	elif grid[pos] == CLEAN:
    		direction = (direction - 1) % 4
    	grid[pos] = (grid[pos] - 1) % 4
        if grid[pos] == INFECTED:
            result += 1
        dr, dc = DIRECTIONS[direction]
    	pos = (pos[0] + dr, pos[1] + dc)

    return result

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
