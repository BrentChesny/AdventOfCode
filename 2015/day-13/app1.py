import re, itertools
rules = [re.match('([A-Z][a-z]+).*(gain|lose)[^0-9]*([0-9]+).*([A-Z][a-z]+)\.', line).groups() for line in open("input.txt")]
happiness = {a[0]: {b[3]: int(b[2]) * (1 if b[1] == 'gain' else -1) for b in rules if b[0] == a[0]} for a in rules}
print max([sum([happiness[x[i]][x[(i-1)%len(x)]] + happiness[x[i]][x[(i+1)%len(x)]] for i in xrange(len(x))]) for x in itertools.permutations(happiness.keys())])