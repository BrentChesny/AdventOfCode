VALID_TRACKS = {'/', '-', '\\', '|', '+'}
TRACK_MAPPING = {
    '<': '-',
    'v': '|',
    '>': '-',
    '^': '|',
}
DIRECTION_MAPPING = {
    '<': (-1, 0),
    'v': (0, 1),
    '>': (1, 0),
    '^': (0, -1),
}
LEFT = 0
STRAIGHT = 1
RIGHT = 2

class Cart:
    def __init__(self, position, direction):
        self.start = position
        self.position = position
        self.direction = direction
        self.next_turn = 0

    def __repr__(self):
        return f'Cart<{id(self)}>(position={self.position}, direction={self.direction}, next_turn={self.next_turn})'

    def move(self):
        x, y = self.position
        dx, dy = self.direction
        self.position = (x + dx, y + dy)

    def turn(self, track):
        if track == '-' or track == '|':
            return
        elif track == '\\':
            if self.direction == (1, 0):
                self.direction = (0, 1)
            elif self.direction == (0, 1):
                self.direction = (1, 0)
            elif self.direction == (-1, 0):
                self.direction = (0, -1)
            elif self.direction == (0, -1):
                self.direction = (-1, 0)
        elif track == '/':
            if self.direction == (1, 0):
                self.direction = (0, -1)
            elif self.direction == (0, 1):
                self.direction = (-1, 0)
            elif self.direction == (-1, 0):
                self.direction = (0, 1)
            elif self.direction == (0, -1):
                self.direction = (1, 0)
        elif track == '+':
            if self.next_turn == LEFT:
                if self.direction == (1, 0):
                    self.direction = (0, -1)
                elif self.direction == (0, 1):
                    self.direction = (1, 0)
                elif self.direction == (-1, 0):
                    self.direction = (0, 1)
                elif self.direction == (0, -1):
                    self.direction = (-1, 0)
            elif self.next_turn == RIGHT:
                if self.direction == (1, 0):
                    self.direction = (0, 1)
                elif self.direction == (0, 1):
                    self.direction = (-1, 0)
                elif self.direction == (-1, 0):
                    self.direction = (0, -1)
                elif self.direction == (0, -1):
                    self.direction = (1, 0)
            self.next_turn = (self.next_turn + 1) % 3


def parse_input():
    carts = []
    tracks = {}
    lines = open('input.txt').readlines()
    for y, line in enumerate(lines):
        for x, track in enumerate(line.strip('\n')):
            if track in VALID_TRACKS:
                tracks[(x, y)] = track
            elif track in TRACK_MAPPING.keys():
                tracks[(x, y)] = TRACK_MAPPING[track]
                carts.append(Cart((x, y), DIRECTION_MAPPING[track]))

    return tracks, carts


def solve_part_one():
    tracks, carts = parse_input()

    while True:
        carts.sort(key=lambda cart: (cart.position[1], cart.position[0]))

        for cart in carts:
            cart.move()
            cart.turn(tracks[cart.position])

        collisions = [cart1 for cart1 in carts for cart2 in carts if cart1.position == cart2.position and cart1 != cart2]
        if collisions:
            return collisions[0].position

def solve_part_two():
    tracks, carts = parse_input()

    while True:
        carts.sort(key=lambda cart: (cart.position[1], cart.position[0]))

        removed = set()
        for i, cart in enumerate(carts):
            if i in removed:
                continue

            cart.move()
            cart.turn(tracks[cart.position])

            for j, c in enumerate(carts):
                if j in removed:
                    continue
                if c.position == cart.position and c != cart:
                    removed.add(i)
                    removed.add(j)

        for i in sorted(removed, reverse=True):
            carts.pop(i)

        if len(carts) == 1:
            return carts[0].position


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
