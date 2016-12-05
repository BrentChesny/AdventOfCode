import hashlib

puzzle_input = 'cxdnnyjw'
password = ''

x = 0
while len(password) != 8:
	m = hashlib.md5()
	m.update('{}{}'.format(puzzle_input, x))
	hash = m.hexdigest()

	if hash[:5] == '00000':
		print x, hash
		password += hash[5]

	x += 1

print password