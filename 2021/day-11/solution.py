def parse_input():
    return [[int(x) for x in line.strip()] for line in open("input.txt")]


def step(octos):
    for r in range(len(octos)):
        for c in range(len(octos[0])):
            octos[r][c] += 1
    flashed = set()
    stop = False
    while not stop:
        stop = True
        for r in range(len(octos)):
            for c in range(len(octos[0])):
                if octos[r][c] > 9 and (r, c) not in flashed:
                    stop = False
                    flashed.add((r, c))
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            if (
                                0 <= r + dr < len(octos)
                                and 0 <= c + dc < len(octos[0])
                                and (dr != 0 or dc != 0)
                            ):
                                octos[r + dr][c + dc] += 1
    for r, c in flashed:
        octos[r][c] = 0
    return octos, flashed


def solve_part_one():
    octos = parse_input()
    flash_count = 0
    for _ in range(100):
        octos, flashed = step(octos)
        flash_count += len(flashed)
    return flash_count


def solve_part_two():
    octos = parse_input()
    s = 1
    while True:
        octos, flashed = step(octos)
        if len(flashed) == len(octos) * len(octos[0]):
            return s
        s += 1


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
