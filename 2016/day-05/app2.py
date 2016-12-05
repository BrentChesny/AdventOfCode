import hashlib
import sys

puzzle_input = 'cxdnnyjw'
password = ['_'] * 8

x = 0
while '_' in password:
	m = hashlib.md5()
	m.update('{}{}'.format(puzzle_input, x))
	hash = m.hexdigest()

	if hash[:5] == '00000':
		index = hash[5]
		val = hash[6]
		
		if index.isdigit():
			index = int(index)
			if index < 8 and password[index] == '_':
				password[index] = val
				sys.stdout.write(''.join(password))
				sys.stdout.flush()  
				sys.stdout.write('\r')

	x += 1

print ''.join(password)
