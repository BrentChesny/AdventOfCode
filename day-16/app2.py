import re
sues = [re.findall("([a-z]+): ([\d]+)", line) for line in open("input.txt")]
info = {x: {y[0]: int(y[1]) for y in [re.findall("([a-z]+): ([\d]+)", line) for line in open("input.txt")][x-1]} for x in xrange(1,501)}
eq = { "children": 3, "samoyeds": 2, "akitas": 0, "vizslas": 0, "cars": 2, "perfumes": 1}
greater = { "cats": 7, "trees": 3}
less = { "pomeranians": 3, "goldfish": 5}
print [s for s,x in info.iteritems() if not [y for y in eq if y in x and eq[y] != x[y]] + [y for y in less if y in x and less[y] <= x[y]] + [y for y in greater if y in x and greater[y] >= x[y]]]
