from hashlib import md5

puzzle_input = 'qzyelonm'

def contains_three_seq(hash):
    for i in xrange(len(hash)-2):
        if hash[i] == hash[i+1] == hash[i+2]:
            return hash[i]
    return False

def contains_five_seq(hash, value):
    for i in xrange(len(hash)-4):
        if hash[i] == hash[i+1] == hash[i+2] == hash[i+3] == hash[i+4] == value:
            return hash[i]
    return False

found = set()
keys = []

x = 0
while len(keys) < 64:
    hash = md5('{}{}'.format(puzzle_input, x)).hexdigest()

    value = contains_three_seq(hash)
    if value:
        for y in xrange(x+1,x+1001):
            hash_next = md5('{}{}'.format(puzzle_input, y)).hexdigest()
            if contains_five_seq(hash_next, value):
                print 'Key found:', x
                keys.append(x)
                break
                
    x += 1

print max(keys)