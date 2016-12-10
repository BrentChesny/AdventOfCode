from collections import defaultdict

instructions = [line.strip() for line in open('input.txt').readlines()]

result = {
	'bot': defaultdict(list),
	'output': defaultdict(list)
}

rules = {}

for instruction in instructions:
	parts = instruction.split()
	if parts[0] == 'bot':
		bot = int(parts[1])
		low = (parts[5], int(parts[6]))		
		high = (parts[10], int(parts[11]))
		rules[bot] = (low, high)		
	else:
		val = int(parts[1])
		bot = int(parts[5])
		result['bot'][bot].append(val)

while True:
	stop = True

	for bot, chips in result['bot'].items():
		if len(chips) == 2:
			stop = False
			low, high = rules[bot]
			min_chip = min(chips)
			max_chip = max(chips)

			if (min_chip == 17 and max_chip == 61):
				print 'Bot {} is responsible for comparing value-17 chips with value-61 chips'.format(bot)

			result[low[0]][low[1]].append(min_chip)
			result[high[0]][high[1]].append(max_chip)
			result['bot'][bot] = []

	if stop:
		break

print result['output'][0][0] * result['output'][1][0] * result['output'][2][0]