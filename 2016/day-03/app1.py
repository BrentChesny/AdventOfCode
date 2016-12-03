import re

count = 0

for line in open('input.txt').readlines():
	a,b,c = map(int, re.findall(r'\d+', line))

	if a + b > c and a + c > b and b + c > a:
		count += 1

print count