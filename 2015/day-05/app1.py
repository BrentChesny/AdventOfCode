print len([x for x in [line.rstrip("\n") for line in open("input.txt")] if sum([x.count(v) for v in "auioe"]) >= 3 and sum([1 for y in [chr(c) for c in xrange(ord('a'), ord('z')+1)] if y+y in x]) > 0 and sum([1 for y in ["ab", "cd", "pq", "xy"] if y in x]) == 0])