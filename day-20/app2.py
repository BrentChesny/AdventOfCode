puzzle = 33100000 / 11
houses = [0 for x in xrange(puzzle)]

for elf in xrange(1,puzzle):
	count = 0
	for i in xrange(elf,puzzle,elf):
		houses[i] += elf
		count += 1
		if count == 50:
			break

for i,house in enumerate(houses):
	if house >= puzzle:
		print i
		break
