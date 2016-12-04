from collections import Counter

def decrypt(name, id):
	return ''.join([chr(((ord(c) - ord('a') + id) % 26) + ord('a')) if c.isalpha() else ' ' for c in name])

for line in open('input.txt').readlines():
	code, checksum = line.split('[')
	parts = code.split('-')
	code = ''.join(parts[:-1])
	name = '-'.join(parts[:-1])
	id = int(parts[-1])
	checksum = checksum[:-2]

	counter = sorted(Counter(code).most_common(), key=lambda x: (-x[1], x[0]))
	computed = ''.join([counter[i][0] for i in range(len(checksum))])

	if computed == checksum:
		decrypted = decrypt(name, id)
		if 'north' in decrypted:
			print decrypted, id
