puzzle = "hxbxwxba"
puzzle = [ord(x) - ord('a') for x in puzzle]
puzzle = list(reversed(puzzle))

def increment(s):
	for x in xrange(len(s)):
		s[x] += 1
		if s[x] >= 26:
			s[x] = 0
		else:
			break

def check(s):
	good = False
	for x in xrange(len(s)-2):
		if s[x] == s[x+1] + 1 and s[x+1] == s[x+2] + 1:
			good = True
			break

	if not good:
		return False

	for x in s:
		if x == ord('i') or x == ord('o') or x == ord('l'):
			return False

	good = False

	for x in xrange(len(s)-1):
		if s[x] == s[x+1]:
			for y in xrange(x+2, len(s)-1):
				if s[y] == s[y+1]:
					good = True
					break

	return good
	
def convert(s):
	return "".join(list(reversed([chr(x + ord('a')) for x in s])))

def next(s):
	while True:
 		increment(s)
 		if check(s): 
 			print convert(s)
 			break

next(puzzle)
next(puzzle)
