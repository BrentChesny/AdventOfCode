lights = [list(line.strip()) for line in open("input.txt")]

h = len(lights)
w = len(lights[0])


for x in xrange(100):
	step = [line[:] for line in lights]
	for i in xrange(len(lights)):
		for j in xrange(len(lights[i])):
			neighbours = 0
			for x in xrange(-1, 2):
				for y in xrange(-1, 2):
					if i+x >= 0 and i+x < h and j+y >= 0 and j+y < w and (x != 0 or y != 0) and lights[i+x][j+y] == "#":
						neighbours += 1
			if lights[i][j] == "#":
				step[i][j] = "#" if neighbours == 2 or neighbours == 3 else "."
			elif lights[i][j] == ".":
				step[i][j] = "#" if neighbours == 3 else "."
	lights = step


print sum([len([x for x in line if x == "#"]) for line in lights])