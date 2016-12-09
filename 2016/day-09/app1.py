import re

puzzle_input = open('input.txt').read().strip()
result = ''


while True:
	parts = re.split('\((\d+)x(\d+)\)', puzzle_input, 1)
	
	if len(parts) <= 1:
		result += puzzle_input
		break

	start, x, y, puzzle_input = parts 

	x = int(x)
	y = int(y)

	result += start + (puzzle_input[:x] * y)
	puzzle_input = puzzle_input[x:]

print len(result)