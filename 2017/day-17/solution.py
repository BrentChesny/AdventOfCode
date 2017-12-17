PUZZLE_INPUT = 380

def solve_part_one():
    buff = [0]
    idx = 0

    for val in range(1, 2018):
        idx = (idx + PUZZLE_INPUT + 1) % len(buff)
        buff.insert(idx, val)

    return buff[idx+1]

def solve_part_two():
    idx = 0
    result = None

    for val in xrange(1, 50000001):
        idx = (idx + PUZZLE_INPUT + 1) % val
        if idx == 0:
            result = val

    return result

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
