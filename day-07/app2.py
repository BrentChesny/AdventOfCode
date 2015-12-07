import re
import collections

def solve(rules):
	d = {}
	q = collections.deque(rules)
	while q:
		a, b = q.pop()
		deps = re.findall("[a-z0-9]+", b);
		y = [x for x in deps if not x.isdigit() and x not in d]
		if not y:
			if "AND" in b:
				d[a] = ((int(deps[0]) if deps[0].isdigit() else d[deps[0]]) & (int(deps[1]) if deps[1].isdigit() else d[deps[1]])) % 65536
			elif "OR" in b:
				d[a] = ((int(deps[0]) if deps[0].isdigit() else d[deps[0]]) | (int(deps[1]) if deps[1].isdigit() else d[deps[1]])) % 65536
			elif "NOT" in b:
				d[a] = 65535 - (int(deps[0]) if deps[0].isdigit() else d[deps[0]])
			elif "RSHIFT" in b:
				d[a] = ((int(deps[0]) if deps[0].isdigit() else d[deps[0]]) >> (int(deps[1]) if deps[1].isdigit() else d[deps[1]])) % 65536
			elif "LSHIFT" in b:
				d[a] = ((int(deps[0]) if deps[0].isdigit() else d[deps[0]]) << (int(deps[1]) if deps[1].isdigit() else d[deps[1]])) % 65536
			else:
				d[a] = int(deps[0]) if deps[0].isdigit() else d[deps[0]]
		else:
			q.appendleft((a,b))
	return d['a']

rules = [(x.split(" -> ")[1], x.split(" -> ")[0]) for x in [line.rstrip("\n") for line in open("input.txt")]]
newrules = [r for r in rules if r != ("b", "44430")]
newrules.append(("b", str(solve(rules))))

print solve(newrules)



