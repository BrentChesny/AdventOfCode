b = [[False for x in xrange(1000)] for y in xrange(1000)]
for a in [(x.split(" ")[0] == "toggle", x.split(" ")[1] == "on", map(int, x.split(" ")[-3].split(",")), map(int, x.split(" ")[-1].split(","))) for x in [line.rstrip("\n") for line in open("input.txt")]]: 
	for x in xrange(a[-2][0], a[-1][0] + 1): 
		for y in xrange(a[-2][1], a[-1][1] + 1): 
			b[x][y] = (not b[x][y] if a[0] else a[1]) 
print sum(map(sum, b))