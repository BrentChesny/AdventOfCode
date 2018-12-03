import re

regex = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
fabric_size = 1000

def parse_input():
    return [map(int, regex.match(line).groups()) for line in open('input.txt')]

def create_fabric():
    fabric = [[set() for _ in range(fabric_size)] for _ in range(fabric_size)];
    for id, x, y, width, height in parse_input():
        for col in range(x, x + width):
            for row in range(y, y + height):
                fabric[row][col].add(id)
    return fabric

def solve_part_one():
    fabric = create_fabric()
    return sum(1 for row in fabric for ids in row if len(ids) > 1)

def solve_part_two():
    fabric = create_fabric()
    overlaps = [False for claim in parse_input()]
    for row in fabric:
        for ids in row:
            if len(ids) > 1:
                for id in ids:
                    overlaps[id-1] = True
    return overlaps.index(False) + 1

def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())

if __name__ == '__main__':
    main()
