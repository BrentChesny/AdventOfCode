from collections import Counter

print ''.join([Counter(s).most_common()[-1][0] for s in zip(*[s.strip() for s in open('input.txt').readlines()])])
