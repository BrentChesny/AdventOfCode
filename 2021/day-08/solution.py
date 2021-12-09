def parse_input():
    notes = []
    for line in open("input.txt").readlines():
        numbers, output = line.strip().split(" | ")
        numbers, output = numbers.split(" "), output.split(" ")
        notes.append(([set(x) for x in numbers], [set(x) for x in output]))
    return notes


def solve_part_one():
    notes = parse_input()
    count = 0
    for _, output in notes:
        for number in output:
            if len(number) in [2, 3, 4, 7]:
                count += 1
    return count


def find(l, pred):
    for x in l:
        if pred(x):
            return x
    return None


#   aaaa
#  b    c
#  b    c
#   dddd
#  e    f
#  e    f
#   gggg
def determine_output(numbers, output):
    cf = find(numbers, lambda x: len(x) == 2)  # 1
    acf = find(numbers, lambda x: len(x) == 3)  # 7
    bdcf = find(numbers, lambda x: len(x) == 4)  # 4
    abcdefg = find(numbers, lambda x: len(x) == 7)  # 8
    eg = abcdefg - acf - bdcf

    acdeg = find(numbers, lambda x: len(x) == 5 and eg.issubset(x))  # 2
    acdfg = find(numbers, lambda x: len(x) == 5 and acf.issubset(x))  # 3
    abdfg = find(
        numbers, lambda x: len(x) == 5 and not eg.issubset(x) and not acf.issubset(x)
    )  # 5
    abdefg = abdfg | eg  # 6
    abcdfg = abdfg | acf  # 9

    def map(n):
        mapping = [None, cf, acdeg, acdfg, bdcf, abdfg, abdefg, acf, abcdefg, abcdfg]
        out = None
        try:
            out = mapping.index(n)
        except ValueError:
            out = 0
        return out

    return (
        map(output[0]) * 1000
        + map(output[1]) * 100
        + map(output[2]) * 10
        + map(output[3])
    )


def solve_part_two():
    return sum(determine_output(*entry) for entry in parse_input())


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
