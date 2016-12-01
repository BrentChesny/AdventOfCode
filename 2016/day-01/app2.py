directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
location = (0, 0)

visited = {location}

for instruction in open('input.txt').read().strip().split(', '):
	direction, steps = instruction[0], int(instruction[1:])

	if direction == 'R':
		directions = directions[1:] + [directions[0]]
	else:
		directions = [directions[-1]] + directions[:-1]

	for _ in range(steps):
		location = (location[0] +  directions[0][0], location[1] + directions[0][1])
		if location in visited:
			print sum(map(abs, location))
		else:
			visited.add(location)



print sum(map(abs, location))