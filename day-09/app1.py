import re, itertools

rules = [re.match('([a-zA-Z]+) to ([a-zA-Z]+) = ([0-9]+)', line).groups() for line in open("input.txt")]
places = set([x[0] for x in rules] + [x[1] for x in rules])

costs = {x: {y: 0 for y in places} for x in places}

for a,b,c in rules:
	costs[a][b] = c
	costs[b][a] = c

print min([sum(map(int, [costs[c[i]][c[i+1]] for i,x in enumerate(c[:-1])])) for c in itertools.permutations(places)])
	
