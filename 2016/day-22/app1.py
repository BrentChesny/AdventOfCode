import re
from collections import namedtuple

Node = namedtuple('Node', ['x', 'y', 'size', 'used', 'available', 'used_percent'])
nodes = map(Node._make, [map(int, re.match('/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%', line).groups()) for line in open('input.txt').readlines()[2:]])

count = 0
for a in nodes:
	for b in nodes:
		if a.used > 0 and a != b and a.used < b.available:
			count += 1

print count

