import re
sues = [re.findall("([a-z]+): ([\d]+)", line) for line in open("input.txt")]
info = {x: {y[0]: int(y[1]) for y in [re.findall("([a-z]+): ([\d]+)", line) for line in open("input.txt")][x-1]} for x in xrange(1,501)}
data = { "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
print [s for s,x in info.iteritems() if not [y for y in data if y in x and data[y] != x[y]]]
