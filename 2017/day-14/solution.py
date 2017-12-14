PUZZLE_INPUT = 'jzgqcdpd'

def solve_part_one():
    used = 0
    for i in range(128):
        used += knot_hash(PUZZLE_INPUT + '-' + str(i)).count('1')
    return used

def solve_part_two():
    grid = []
    for i in range(128):
        h = knot_hash(PUZZLE_INPUT + '-' + str(i))
        grid.append(map(int, h))

    result = 0
    for row in range(128):
        for col in range(128):
            if grid[row][col] == 1:
                result += 1
                flood_region(grid, row, col)

    return result

def knot_hash(s):
    lengths = map(ord, s) + [17, 31, 73, 47, 23]
    h = list(range(256))
    n = len(h)
    skip, index = 0, 0

    for i in range(64):
        for l in lengths:
            for k in range(l/2):
                i, j = (index + k) % n, (index + l - k - 1) % n
                h[i], h[j] = h[j], h[i]
            index += l + skip
            skip += 1

    dense_hash = []
    for block in range(16):
        y = 0
        for x in h[block*16:(block+1)*16]:
            y ^= x
        dense_hash.append(y)

    return ''.join(format(x, '08b') for x in dense_hash)

def flood_region(grid, row, col):
    queue = [(row, col)]
    while queue:
        r, c = queue.pop(0)
        grid[r][c] = 0
        if valid(r-1, c) and grid[r-1][c]:
            queue.append((r-1, c))
        if valid(r+1, c) and grid[r+1][c]:
            queue.append((r+1, c))
        if valid(r, c-1) and grid[r][c-1]:
            queue.append((r, c-1))
        if valid(r, c+1) and grid[r][c+1]:
            queue.append((r, c+1))

def valid(row, col):
    return 0 <= row < 128 and 0 <= col < 128

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
