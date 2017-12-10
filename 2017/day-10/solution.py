def solve_part_one():
    lengths = map(int, open('input.txt').read().strip().split(','))
    h = list(range(256))

    knot_hash(h, lengths)

    return h[0] * h[1]

def solve_part_two():
    lengths = map(ord, open('input.txt').read().strip())
    lengths += [17, 31, 73, 47, 23]
    h = list(range(256))
    skip, index = 0, 0

    for i in range(64):
        skip, index = knot_hash(h, lengths, skip, index)

    dense_hash = []
    for block in range(16):
        y = 0
        for x in h[block*16:(block+1)*16]:
            y ^= x
        dense_hash.append(y)

    return ''.join('%0.2x' % x for x in dense_hash)


def knot_hash(h, lengths, skip=0, index=0):
    n = len(h)

    for l in lengths:
        for k in range(l/2):
            i, j = (index + k) % n, (index + l - k - 1) % n
            h[i], h[j] = h[j], h[i]
        index += l + skip
        skip += 1

    return skip, index


def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
