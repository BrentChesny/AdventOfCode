def parse_input():
    return [line.strip() for line in open("input.txt").readlines()]


def solve_part_one():
    report = parse_input()
    counts = [(pos.count("0"), pos.count("1")) for pos in zip(*report)]
    gamma = int("".join("0" if count[0] > count[1] else "1" for count in counts), 2)
    epsilon = int("".join("0" if count[0] < count[1] else "1" for count in counts), 2)
    return gamma * epsilon


def solve_part_two():
    report = parse_input()
    oxygen_generator_rating = calculate_rating(report, filter_most_common)
    c02_scrubber_rating = calculate_rating(report, filter_least_common)
    return oxygen_generator_rating * c02_scrubber_rating


def calculate_rating(report, criteria):
    bit = 0
    while len(report) > 1:
        report = criteria(report, bit)
        bit += 1
    return int(report[0], 2)


def filter_most_common(numbers, bit):
    bits = [number[bit] for number in numbers]
    keep = "0" if bits.count("0") > bits.count("1") else "1"
    f = lambda number: number[bit] == keep
    return [number for number in numbers if f(number)]


def filter_least_common(numbers, bit):
    bits = [number[bit] for number in numbers]
    keep = "0" if bits.count("0") <= bits.count("1") else "1"
    f = lambda number: number[bit] == keep
    return [number for number in numbers if f(number)]


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
