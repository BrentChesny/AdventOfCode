from itertools import permutations

grid = [line.strip() for line in open('input.txt').readlines()]
locations = []
distances = {}
start = None

def calc_distance(begin, end):
	queue = [(0, begin)]
	visited = {begin}
	
	while queue:
		distance, location = queue.pop(0)
		r, c = location

		if location == end:
			return distance

		for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
			new_r, new_c = r + dr, c + dc
			if grid[new_r][new_c] != '#' and not (new_r, new_c) in visited:
				queue.append((distance+1, (new_r, new_c)))
				visited.add((new_r, new_c))

for row in xrange(len(grid)):
    for col in xrange(len(grid[row])):
        if grid[row][col].isdigit():
            locations.append((row, col))
        if grid[row][col] == '0':
            start = (row, col)

for a in locations:
	for b in locations:
		distances[(a,b)] = calc_distance(a, b)


locations.remove(start)

results = []
for perm in permutations(locations):
	prev = start
	dist = 0
	for loc in perm:
		dist += distances[(prev, loc)]
		prev = loc

	dist += distances[(prev, start)]
	results.append(dist)

print min(results)
