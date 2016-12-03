import re

count = 0

lines = open('input.txt').readlines()
groups = [lines[i:i+3] for i in range(0,len(lines),3)]

for group in groups:
	a, d, g = map(int, re.findall(r'\d+', group[0]))
	b, e, h = map(int, re.findall(r'\d+', group[1]))
	c, f, i = map(int, re.findall(r'\d+', group[2]))

	if a + b > c and a + c > b and b + c > a:
		count += 1

	if d + e > f and d + f > e and e + f > d:
		count += 1

	if g + h > i and g + i > h and h + i > g:
		count += 1

print count