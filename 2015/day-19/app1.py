import re
lines = [line.strip() for line in open("input.txt")]
rules = lines[:-2]
mol = lines[-1]

rules = [re.match('([a-zA-Z]+) => ([a-zA-Z]+)', x).groups() for x in rules]

count = 0
mols = []

print mol, '\n'

for rule in rules:
	l = -1
	f = 9999
	while f != -1:
		f = mol.find(rule[0], l +1)
		if f != -1:
			#print f, mol[0:f], rule[1], mol[f+len(rule[0]):]
			nmol = mol[0:f] + rule[1] + mol[f+len(rule[0]):]
			mols.append(nmol)
			l = f

print mols
print len(set(mols))