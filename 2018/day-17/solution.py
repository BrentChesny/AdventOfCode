from collections import namedtuple
from itertools import count
import re

LEFT = 0
RIGHT = 1
DOWN = 2

class Pos(namedtuple('Pos', ['x', 'y'])):
    def down(self):
        return Pos(self.x, self.y + 1)

    def left(self):
        return Pos(self.x - 1, self.y)

    def right(self):
        return Pos(self.x + 1, self.y)

    def next(self, direction):
        if direction == LEFT:
            return self.left()
        elif direction == RIGHT:
            return self.right()
        elif direction == DOWN:
            return self.down();

def parse_input():
    grid = {}
    for line in open('input.txt'):
        a, b, c, d, e = re.match('(.)=(\d+), (.)=(\d+)\.\.(\d+)', line).groups()
        if a == 'x':
            x = int(b)
            for y in range(int(d), int(e) + 1):
                grid[Pos(x, y)] = '#'
        else:
            y = int(b)
            for x in range(int(d), int(e) + 1):
                grid[Pos(x, y)] = '#'
    return grid

def drop(grid, limit, pos, direction):
    horizontal = True
    while True:
        if pos.y > limit:
            return

        grid[pos] = '|'

        if grid.get(pos.down(), '.') in ['.', '|']:
            horizontal = False
            direction = DOWN

        next_pos = pos.next(direction)
        next = grid.get(next_pos, '.')

        if next in ['.', '|']:
            pos = next_pos
        elif direction == DOWN:
            if grid.get(pos.left(), '.') != '#':
                l = drop(grid, limit, pos.left(), LEFT)
            else:
                l = pos
            if grid.get(pos.right(), '.') != '#':
                r = drop(grid, limit, pos.right(), RIGHT)
            else:
                r = pos
            if l and r:
                settle(grid, l, r)
            break
        else:
            break
    return pos if horizontal else None

def settle(grid, left, right):
    lx, ly = left
    rx, _ = right
    for x in range(lx, rx + 1):
        grid[Pos(x, ly)] = '~'

def count_wet(grid, min_y, max_y):
    return len([c for pos, c in grid.items() if c in ['|', '~'] and min_y <= pos.y <= max_y ])

def count_settled(grid, min_y, max_y):
    return len([c for pos, c in grid.items() if c == '~' and min_y <= pos.y <= max_y ])

def solve():
    grid = parse_input()
    min_y = min(pos.y for pos in grid.keys())
    max_y = max(pos.y for pos in grid.keys())

    wet_count = 0
    for _ in count():
        drop(grid, max_y, Pos(500, 0), DOWN)
        new_count = count_wet(grid, min_y, max_y)
        if new_count == wet_count:
            print('Part one:', wet_count)
            print('Part two:', count_settled(grid, min_y, max_y))
            return
        else:
            wet_count = new_count

def main():
    solve()

if __name__ == '__main__':
    main()
