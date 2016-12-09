import re

puzzle_input = open('input.txt').read().strip()


def decompress(puzzle):
	result = 0

	while True:
		parts = re.split('\((\d+)x(\d+)\)', puzzle, 1)
		
		if len(parts) <= 1:
			result += len(puzzle)
			break

		start, x, y, puzzle = parts 

		x = int(x)
		y = int(y)

		result += len(start)
		result += decompress(puzzle[:x]) * y
		puzzle = puzzle[x:]

	return result

print decompress(puzzle_input)