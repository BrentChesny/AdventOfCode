from operator import mul

packages = sorted([int(line) for line in open('input.txt')], reverse=True)
weight = sum(packages) / 4

size = 99
eq = 99999999999999999

def e(packages):
	return reduce(mul, packages) if packages else 99999999999999

def pack(part1, packages):
	global size, eq

	if (len(part1) > size or e(part1) >= eq or sum(part1) > weight):
		return

	if not packages:
		if (sum(part1) == weight and (len(part1) < size or (len(part1) == size and e(part1) < eq))):
			size = len(part1)
			eq = e(part1)
		return

	package, tail = packages[0], packages[1:]
	pack(part1 + [package], tail)	
	pack(part1, tail)	


pack([], packages)
print eq