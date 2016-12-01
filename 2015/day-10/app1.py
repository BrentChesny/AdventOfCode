puzzle = "3113322113"

for x in xrange(40):
	count = 1
	result = ""
	for i in xrange(1, len(puzzle)):
		if puzzle[i] != puzzle[i-1]:
			result += str(count) + puzzle[i-1]
			count = 1
		else:
			count += 1
	puzzle = result + str(count) + puzzle[-1]
print len(puzzle)