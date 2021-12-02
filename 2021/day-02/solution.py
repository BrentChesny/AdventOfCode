def parse_input():
    course = []
    for line in open("input.txt").readlines():
        direction, steps = line.split(" ")
        course.append((direction, int(steps)))
    return course


def solve_part_one():
    h_pos, depth = 0, 0
    for direction, steps in parse_input():
        if direction == "forward":
            h_pos += steps
        elif direction == "up":
            depth -= steps
        elif direction == "down":
            depth += steps
    return h_pos * depth


def solve_part_two():
    h_pos, depth, aim = 0, 0, 0
    for direction, steps in parse_input():
        if direction == "forward":
            h_pos += steps
            depth += aim * steps
        elif direction == "up":
            aim -= steps
        elif direction == "down":
            aim += steps
    return h_pos * depth


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
