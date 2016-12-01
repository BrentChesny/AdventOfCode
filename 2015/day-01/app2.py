l = raw_input()
print [i+1 for i in xrange(len(l)) if (sum([1 if x == '(' else -1 for x in l][0:i+1]) == -1)][0]
