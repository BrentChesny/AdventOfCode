from collections import defaultdict


def parse_input():
    caves = defaultdict(list)
    for line in open("input.txt"):
        fr, to = line.strip().split("-")
        caves[fr].append(to)
        caves[to].append(fr)
    return caves


def is_small(cave):
    return cave.islower()


def solve(caves, current, visited):
    if current == "end":
        return 1
    paths = 0
    for destination in caves[current]:
        if is_small(destination) and destination in visited:
            continue
        paths += solve(caves, destination, set(visited | {current}))
    return paths


def solve_part_one():
    caves = parse_input()
    return solve(caves, "start", set())


def solve_with_revisit(caves, current, visited, revisited):
    if current == "end":
        return 1
    paths = 0
    for destination in caves[current]:
        if is_small(destination):
            if destination in visited:
                if revisited:
                    continue
                else:
                    if destination not in ["start", "end"]:
                        paths += solve_with_revisit(
                            caves, destination, set(visited | {current}), destination
                        )
            else:
                paths += solve_with_revisit(
                    caves, destination, set(visited | {current}), revisited
                )
        else:
            paths += solve_with_revisit(
                caves, destination, set(visited | {current}), revisited
            )
    return paths


def solve_part_two():
    caves = parse_input()
    return solve_with_revisit(caves, "start", set(), None)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
