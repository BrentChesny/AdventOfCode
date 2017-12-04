def solve_part_one():
    result = 0
    for line in open('input.txt').readlines():
        words = line.strip().split()
        result += 1 if len(words) == len(set(words)) else 0

    return result

def solve_part_two():
    result = 0
    for line in open('input.txt').readlines():
        words = [tuple(sorted(word)) for word in line.strip().split()]
        result += 1 if len(words) == len(set(words)) else 0

    return result

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
