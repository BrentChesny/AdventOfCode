def parse_input():
    lines = [line.strip() for line in open("input.txt")]
    pixels = set()
    for x, line in enumerate(lines[2:]):
        for y, c in enumerate(line):
            if c == "#":
                pixels.add((x, y))
    return lines[0], pixels


def enhance(img, algo, infinite_bit):
    min_x = min(x for x, _ in img)
    max_x = max(x for x, _ in img)
    min_y = min(y for _, y in img)
    max_y = max(y for _, y in img)

    new_img = set()
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            bits = ""
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    bits += (
                        "1"
                        if (x + dx, y + dy) in img
                        else (
                            "0"
                            if min_x <= x + dx <= max_x and min_y <= y + dy <= max_y
                            else infinite_bit
                        )
                    )
            i = int(bits, 2)
            if algo[i] == "#":
                new_img.add((x, y))
    return new_img


def solve_part_one():
    algo, img = parse_input()
    for i in range(2):
        img = enhance(img, algo, "0" if i % 2 == 0 else "1")
    return len(img)


def solve_part_two():
    algo, img = parse_input()
    for i in range(50):
        img = enhance(img, algo, "0" if i % 2 == 0 else "1")
    return len(img)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
