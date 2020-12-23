from collections import deque

INPUT = [int(c) for c in "589174263"]

# Naive implementation for part 1 :)
def solve_part_one():
    cups = deque(INPUT)
    for _ in range(100):
        cups = list(cups)
        # take 3 cups next to current cup
        taken, rest = cups[1:4], [cups[0]] + cups[4:]

        # move
        dest = rest[0] - 1
        if dest == 0:
            dest = 9
        while dest in taken:
            dest -= 1
            if dest == 0:
                dest = 9
        idx = rest.index(dest)
        cups = rest[: idx + 1] + taken + rest[idx + 1 :]

        cups = deque(cups)

        # next current cup
        cups.rotate(-1)

    idx = cups.index(1)
    cups.rotate(-idx)

    return "".join(str(c) for c in list(cups)[1:])


class Cup:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def build_list():
    cups = [None] * (1000001)
    values = INPUT + list(range(10, 1000001))

    first = values[0]
    cups[first] = Cup(first)
    first = cups[first]
    prev = first

    for value in values[1:]:
        cur = cups[value] = Cup(value)
        cur.prev = prev
        prev.next = cur
        prev = cur

    prev.next = first

    return first, cups


def play(cur, cups, moves):
    maxcup = len(cups) - 1

    for _ in range(moves):
        # Pick up 3 cups
        first = cur.next
        mid = first.next
        last = mid.next
        picked = (first.value, mid.value, last.value)

        # Remove them from the list
        cur.next = last.next
        cur.next.prev = cur

        # Select the destination cup value, after which we'll insert the 3 picked cups
        dst = maxcup if cur.value == 1 else cur.value - 1
        while dst in picked:
            dst = maxcup if dst == 1 else dst - 1

        # Get the corresponding cup from its value
        dst = cups[dst]

        # Insert the picked cups right after it
        first.prev = dst
        last.next = dst.next
        dst.next.prev = last
        dst.next = first

        # Advance the current cup
        cur = cur.next


# As could be expected, part 2 uses huge numbers so we need to be clever: linked list instead of deque
def solve_part_two():
    current, cups = build_list()
    play(current, cups, 10_000_000)
    return cups[1].next.value * cups[1].next.next.value


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
