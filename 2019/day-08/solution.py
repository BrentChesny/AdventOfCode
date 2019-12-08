W = 25
H = 6


def parse_input():
    image = list(map(int, open('input.txt').readline().strip()))
    return [image[i:i + W*H] for i in range(0, len(image), W*H)]


def decode(image):
    result = image.pop()
    for layer in reversed(image):
        for i in range(W*H):
            if layer[i] != 2:
                result[i] = layer[i]
    return result


def print_image(image):
    image = decode(image)
    for h in range(H):
        for w in range(W):
            print('#' if image[h*W+w] == 1 else ' ', end='')
        print()


def solve_part_one():
    image = parse_input()
    layer = min(image, key=lambda l: l.count(0))
    return layer.count(1) * layer.count(2)


def solve_part_two():
    image = parse_input()
    print_image(image)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ')
    solve_part_two()


if __name__ == '__main__':
    main()
