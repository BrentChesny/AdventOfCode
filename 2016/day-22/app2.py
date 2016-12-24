import re
from collections import namedtuple

Node = namedtuple('Node', ['x', 'y', 'size', 'used', 'available', 'used_percent'])
nodes = map(Node._make, [map(int, re.match('/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%', line).groups()) for line in open('input.txt').readlines()[2:]])

max_x = max(node.x for node in nodes)
max_y = max(node.y for node in nodes)
grid = [[' ' for _ in range(max_x+1)] for j in range(max_y+1)]

for node in nodes:
	if node.size > 400:
		grid[node.y][node.x] = '#'
	elif node.used > 0:
		grid[node.y][node.x] = '.'
	elif node.used == 0:
		grid[node.y][node.x] = '@'

grid[0][max_x] = 'T'

for line in grid:
	print ' '.join(line)

# Solved by hand:
# 	1) Count how many moves to place empty node to left of target node: 66
# 	2) Count how many moves to move target node one place to the left: 5
# 	3) Calculate how many times to do step 2 to move empty cell to the first node: 35
#   4) Do one last move to move target node, which is next to empty node, into the first node: 1
# 	Result: 66 + 35 * 5 + 1 = 242



