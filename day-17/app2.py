import itertools, collections
sizes = [int(line) for line in open("input.txt")]

count = collections.defaultdict(int)

for x in itertools.product(range(2), repeat=len(sizes)):
	num = sum(x)
	if sum([x[y] * sizes[y] for y in xrange(len(sizes))]) == 150:
		count[num] += 1

print count[min(count.keys())]