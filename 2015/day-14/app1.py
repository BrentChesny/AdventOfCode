import re
deer = [d + [d[1], d[2], True, 0] for d in [list(map(int, re.match('[^\d]+([\d]+)[^\d]+([\d]+)[^\d]+([\d]+)[^\d]+', line).groups())) for line in open("input.txt")]]

def run(d,s):
	d[6] += d[0] if d[5] else 0
	if d[5]:
		d[3] -= 1
		if d[3] == 0:
			d[5] = False
			d[3] = d[1]
	else:
		d[4] -= 1
		if d[4] == 0:
			d[5] = True
			d[4] = d[2]

for s in xrange(1, 2504):
	for d in deer:
		run(d, s)

print max([d[6] for d in deer])

