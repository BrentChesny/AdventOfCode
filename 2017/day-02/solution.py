def solve_part_one():
    lines = [map(int, line.split()) for line in open('input.txt').readlines()]
    return sum(max(line) - min(line) for line in lines)


def solve_part_two():
    lines = [map(int, line.split()) for line in open('input.txt').readlines()]

    result = 0
    for line in lines:
        for i in range(len(line)):
            for j in range(len(line)):
                if i != j and line[i] > line[j] and line[i] % line[j] == 0:
                    result += line[i] / line[j]

    return result

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
