from collections import Counter

messages = [s.strip() for s in open('input.txt').readlines()]
messages = zip(*messages)

decoded = [Counter(s).most_common()[0][0] for s in messages]

print ''.join(decoded)
