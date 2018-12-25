from functools import lru_cache
from collections import deque
import heapq


ROCKY = '.'
WET = '='
NARROW = '|'

RISK_LEVELS = {
    ROCKY: 0,
    WET: 1,
    NARROW: 2,
}

TORCH = 'torch'
CLIMBING_GEAR = 'climbing_gear'
NEITHER = 'neither'

ALLOWED_TOOLS = {
    ROCKY: [TORCH, CLIMBING_GEAR],
    WET: [NEITHER, CLIMBING_GEAR],
    NARROW: [TORCH, NEITHER],
}

def parse_input():
    lines = open('input.txt').read().strip().split('\n')
    depth = int(lines[0].split(' ')[1])
    target = tuple(map(int, lines[1].split(' ')[1].split(',')))
    return depth, target

@lru_cache(maxsize=1000000)
def region_type(pos, depth, target):
    modulo = erosion_level(pos, depth, target) % 3
    if modulo == 0:
        return ROCKY
    elif modulo == 1:
        return WET
    elif modulo == 2:
        return NARROW

@lru_cache(maxsize=1000000)
def erosion_level(pos, depth, target):
    idx = geologic_index(pos, depth, target)
    return (idx + depth) % 20183

@lru_cache(maxsize=1000000)
def geologic_index(pos, depth, target):
    x, y = pos
    if pos == (0, 0) or pos == target:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return erosion_level((x-1, y), depth, target) * erosion_level((x, y-1), depth, target)

def solve_part_one():
    depth, target = parse_input()
    target_x, target_y = target

    risk = 0
    for y in range(0, target_y + 1):
        for x in range(0, target_x + 1):
            pos = (x, y)
            type = region_type(pos, depth, target)
            risk += RISK_LEVELS[type]

    return risk

def solve_part_two():
    depth, target = parse_input()
    start = (0, 0, TORCH)
    visiting = [(0, start)]
    best = dict()

    while visiting:
        dist, state = heapq.heappop(visiting)
        x, y, tool = state
        type = region_type((x, y), depth, target)
        if state in best and best[state] <= dist:
            continue
        best[state] = dist
        if (x, y) == target and tool == TORCH:
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_y < 0:
                continue
            next_type = region_type((next_x, next_y), depth, target)
            if tool not in ALLOWED_TOOLS[next_type]:
                continue
            next = (next_x, next_y, tool)
            next_dist = dist + 1
            if next in best and best[next] <= next_dist:
                continue
            heapq.heappush(visiting, (next_dist, next))
        for next_tool in ALLOWED_TOOLS[type]:
            if tool == next_tool:
                continue
            next = (x, y, next_tool)
            next_dist = dist + 7
            if next in best and best[next] <= next_dist:
                continue
            heapq.heappush(visiting, (next_dist, next))

    return best[(target[0], target[1], TORCH)]

def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
