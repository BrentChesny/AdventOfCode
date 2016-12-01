directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
location = (0, 0)

for instruction in open('input.txt').read().strip().split(', '):
	direction, steps = instruction[0], int(instruction[1:])

	if direction == 'R':
		directions = directions[1:] + [directions[0]]
	else:
		directions = [directions[-1]] + directions[:-1]

	location = (location[0] + steps * directions[0][0], location[1] + steps * directions[0][1])

print sum(map(abs, location))