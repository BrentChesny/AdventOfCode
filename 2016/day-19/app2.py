puzzle_input = 3012210

elves = range(1,puzzle_input+1)

index = 0

while len(elves) > 1:
	if len(elves) % 1000 == 0:
		print len(elves)
	target = (index + len(elves)/2) % len(elves)
	del elves[target]

	if target > index:
		index = (index + 1) 
	index %= len(elves)
	
print elves[0]

