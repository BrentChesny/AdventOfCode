def parse_input():
    return [list(line.strip('\n')) for line in open('input.txt').readlines()]

def solve_part_one():
    grid = parse_input()
    pos_r, pos_c = 0, grid[0].index('|')
    dir_r, dir_c = 1, 0
    result = ''

    while grid[pos_r+dir_r][pos_c+dir_c] != ' ':
        pos_r, pos_c = pos_r + dir_r, pos_c + dir_c
        if grid[pos_r][pos_c].isupper():
            result += grid[pos_r][pos_c]

        if grid[pos_r][pos_c] == '+':
            dir_r, dir_c = find_new_direction(grid, (pos_r, pos_c), (dir_r, dir_c))

    return result

def solve_part_two():
    grid = parse_input()
    pos_r, pos_c = 0, grid[0].index('|')
    dir_r, dir_c = 1, 0
    result = 1

    while grid[pos_r+dir_r][pos_c+dir_c] != ' ':
        result += 1
        pos_r, pos_c = pos_r + dir_r, pos_c + dir_c

        if grid[pos_r][pos_c] == '+':
            dir_r, dir_c = find_new_direction(grid, (pos_r, pos_c), (dir_r, dir_c))

    return result

def find_new_direction(grid, pos, old_dir):
    pos_r, pos_c = pos
    if grid[pos_r-1][pos_c] == '|' and old_dir != (1, 0):
        return -1, 0
    if grid[pos_r+1][pos_c] == '|' and old_dir != (-1, 0):
        return 1, 0
    if grid[pos_r][pos_c-1] == '-' and old_dir != (0, 1):
        return 0, -1
    if grid[pos_r][pos_c+1] == '-' and old_dir != (0, -1):
        return 0, 1


def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
