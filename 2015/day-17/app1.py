import itertools
sizes = [int(line) for line in open("input.txt")]

count = 0

for x in itertools.product(range(2), repeat=len(sizes)):
	if sum([x[y] * sizes[y] for y in xrange(len(sizes))]) == 150:
		count += 1
print count