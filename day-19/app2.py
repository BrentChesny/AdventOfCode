import re

lines = [line.strip() for line in open("input.txt")]
rules = lines[:-2]
mol = lines[-1]
rules = [re.match('([a-zA-Z]+) => ([a-zA-Z]+)', x).groups() for x in rules]
mn = 99999999999

def a(m, count):
	global mn
	if count > mn:
		return

	if m == "e":
		#print m, count
		if count < mn:
			mn = count
			print mn
		return

	for rule in rules:
		l = -1
		f = 9999
		while f != -1:
			f = m.find(rule[1], l +1)
			if f != -1:
				#print f, m[0:f], rule[1], m[f+len(rule[0]):]
				nm = m[0:f] + rule[0] + m[f+len(rule[1]):]
				a(nm, count+1)
				l = f


a(mol, 0)
print mn
