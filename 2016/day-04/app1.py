from collections import Counter

result = 0

for line in open('input.txt').readlines():
	code, checksum = line.split('[')
	parts = code.split('-')
	code = ''.join(parts[:-1])
	id = int(parts[-1])
	checksum = checksum[:-2]

	counter = sorted(Counter(code).most_common(), key=lambda x: (-x[1], x[0]))
	cs = ''.join([counter[i][0] for i in range(len(checksum))])

	if cs == checksum:
		result += id


print result