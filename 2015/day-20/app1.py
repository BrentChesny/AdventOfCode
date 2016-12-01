puzzle = 33100000 / 10
houses = [0 for x in xrange(puzzle)]

for elf in xrange(1,puzzle):
	for i in xrange(elf,puzzle,elf):
		houses[i] += elf

for i,house in enumerate(houses):
	if house >= puzzle:
		print i
		break
