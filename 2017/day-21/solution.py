from math import sqrt

def parse_input():
    patterns = dict()
    for line in open('input.txt').readlines():
        i, o = line.strip().split(' => ')
        i = map(tuple, i.split('/'))
        o = map(list, o.split('/'))
        for _ in xrange(4):
            patterns[tuple(i)] = o
            patterns[flip_horizontal(i)] = o
            patterns[flip_vertical(i)] = o
            i = rotate(i)
    return patterns

def solve_part_one():
    grid = map(list, ['.#.', '..#', '###'])
    patterns = parse_input()

    for _ in xrange(5):
        grid = step(grid, patterns)

    return sum([line.count('#') for line in grid])

def solve_part_two():
    grid = map(list, ['.#.', '..#', '###'])
    patterns = parse_input()

    for _ in xrange(18):
        grid = step(grid, patterns)

    return sum([line.count('#') for line in grid])

def rotate(matrix):
    return tuple(map(tuple, zip(*matrix[::-1])))

def flip_horizontal(matrix):
    return tuple([tuple(row[::-1]) for row in matrix])

def flip_vertical(matrix):
    return tuple(map(tuple, matrix[::-1]))

def decompose(matrix, size):
    parts = []
    for i in xrange(len(matrix)/size):
        for j in xrange(len(matrix[0])/size):
            parts.append([[matrix[size*i+r][size*j+c] for c in xrange(size)] for r in xrange(size)])
    return parts

def compose(parts):
    matrix = []
    size = len(parts[0])
    for i in xrange(int(sqrt(len(parts)))):
        for r in xrange(size):
            line = []
            for j in xrange(int(sqrt(len(parts)))):
                line += parts[i*int(sqrt(len(parts)))+j][r]
            matrix.append(line)
    return matrix

def step(matrix, patterns):
    size = 2 if len(matrix) % 2 == 0 else 3
    parts = decompose(matrix, size)
    new_parts = []
    for part in parts:
        new_parts.append(patterns[tuple(map(tuple, part))])
    return compose(new_parts)

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
