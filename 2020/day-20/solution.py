N = 12


def parse_input():
    tiles = dict()
    for raw_tile in open("input.txt").read().split("\n\n"):
        lines = raw_tile.splitlines()
        tile_id = int(lines[0].strip("Tile ").strip(":"))
        tile = lines[1:]
        top = tile[0]
        right = "".join(t[-1] for t in tile)
        bottom = tile[-1][::-1]
        left = "".join(t[0] for t in tile)[::-1]
        content = [line[1:-1] for line in tile[1:-1]]
        tiles[tile_id] = (top, right, bottom, left, content)
    return tiles


def solve_part_one():
    tiles = parse_input()
    solution = solve([], set(tiles.keys()), tiles)
    return (
        solution[0][0]
        * solution[N - 1][0]
        * solution[N * (N - 1)][0]
        * solution[N * N - 1][0]
    )


# board = [(tile_id, flip, turns, right, bottom)]
def solve(board, left, tiles):
    if len(left) == 0:
        return board
    for tile_id, flip, turns, rt, bt in fits(board, left, tiles):
        s = solve(board + [(tile_id, flip, turns, rt, bt)], left - {tile_id}, tiles)
        if s:
            return s


def fits(board, left, tiles):
    # Determine constraints to fit the current board
    rt = None
    bt = None
    if len(board) == 0:
        pass
    elif len(board) < N:
        rt = board[-1][3]
    else:
        bt = board[len(board) - N][4]
        if len(board) % N:
            rt = board[-1][3]

    # Find all tiles that fit these constraints
    options = []
    for tile_id in left:
        for orientation in orientations(tiles[tile_id]):
            option = (
                tile_id,
                orientation[0],
                orientation[1],
                orientation[3][::-1],
                orientation[4][::-1],
            )
            if rt and bt:
                if orientation[5] == rt and orientation[2] == bt:
                    options.append(option)
            elif rt:
                if orientation[5] == rt:
                    options.append(option)
            elif bt:
                if orientation[2] == bt:
                    options.append(option)
            else:
                options.append(option)
    return options


def orientations(tile):
    top, right, bottom, left, _ = tile
    return [
        (False, 0, top, right, bottom, left),
        (False, 1, left, top, right, bottom),
        (False, 2, bottom, left, top, right),
        (False, 3, right, bottom, left, top),
        (True, 0, top[::-1], left[::-1], bottom[::-1], right[::-1]),
        (True, 1, right[::-1], top[::-1], left[::-1], bottom[::-1]),
        (True, 2, bottom[::-1], right[::-1], top[::-1], left[::-1]),
        (True, 3, left[::-1], bottom[::-1], right[::-1], top[::-1]),
    ]


monster = [
    (0, 18),
    (1, 0),
    (1, 5),
    (1, 6),
    (1, 11),
    (1, 12),
    (1, 17),
    (1, 18),
    (1, 19),
    (2, 1),
    (2, 4),
    (2, 7),
    (2, 10),
    (2, 13),
    (2, 16),
]


def solve_part_two():
    tiles = parse_input()
    solution = solve([], set(tiles.keys()), tiles)
    image = construct_image(solution, tiles)

    for flip, turns in [
        (False, 0),
        (False, 1),
        (False, 2),
        (False, 3),
        (True, 0),
        (True, 1),
        (True, 2),
        (True, 3),
    ]:
        oriented_image = orientate(image, flip, turns, N)
        monster_pixels = 0

        for r in range(8 * N - 2):
            for c in range(8 * N - 19):
                is_monster = True
                for dr, dc in monster:
                    if oriented_image[r + dr][c + dc] != "#":
                        is_monster = False
                        break
                if is_monster:
                    monster_pixels += len(monster)

        if monster_pixels > 0:
            total = sum(line.count("#") for line in oriented_image)
            return total - monster_pixels


def construct_image(solution, tiles):
    image = []
    rows = [solution[n : n + N] for n in range(0, N * N, N)]
    for row in rows:
        for i in range(8):
            image.append(
                "".join(
                    orientate(tiles[tile_id][4], flip, turns)[i]
                    for tile_id, flip, turns, _, _ in row
                )
            )
    return image


def orientate(content, flip, turns, N=1):
    if flip:
        content = [line[::-1] for line in content]

    for _ in range(turns):
        content = ["".join(row[i] for row in content)[::-1] for i in range(8 * N)]

    return content


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
