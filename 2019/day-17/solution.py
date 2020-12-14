from os import sep
from intcode import IntCodeProcessor
from collections import defaultdict


def parse_input():
    return list(map(int, open("input.txt").readline().split(",")))


def is_intersection(scaffold, x, y):
    return (
        (x - 1, y) in scaffold
        and (x + 1, y) in scaffold
        and (x, y - 1) in scaffold
        and (x, y + 1) in scaffold
    )


def solve_part_one():
    program = parse_input()
    input = []
    computer = IntCodeProcessor(program, input)

    scaffold = set()

    while not computer.is_halted():
        output = computer.execute()

        x, y = 0, 0
        for c in output:
            if chr(c) == "#":
                scaffold.add((x, y))
            if chr(c) == "\n":
                x = 0
                y += 1
            else:
                x += 1

    return sum(x * y for x, y in scaffold if is_intersection(scaffold, x, y))


# Solved this one by hand:
#
# Print the initial output of the droid.
# The desired path is just going straight until you hit an edge.
# At each edge there's only one possible other direction to take.
#
# The following instructions are needed to follow this path:
# R,10,R,10,R,6,R,4,R,10,R,10,L,4,R,10,R,10,R,6,R,4,R,4,L,4,L,10,L,10,R,10,R,10,R,6,R,4,R,10,R,10,L,4,R,4,L,4,L,10,L,10,R,10,R,10,L,4,R,4,L,4,L,10,L,10,R,10,R,10,L,4,
#
# This can be cut up into movement function like so:
#
#   BABCBACACA
#
# where
#
#   A = R,10,R,10,L,4
#   B = R,10,R,10,R,6
#   C = R,4,L,4,L,10,L,10
def solve_part_two():
    program = parse_input()
    program[0] = 2
    inp = []
    computer = IntCodeProcessor(program, inp)

    while not computer.is_halted():
        output = computer.execute()
        for c in output:
            if c < 128:
                print(chr(c), sep="", end="")
            else:
                return c

        main_routine = "B,A,B,C,B,A,C,A,C,A\n"
        A = "R,10,R,10,L,4\n"
        B = "R,10,R,10,R,6,R,4\n"
        C = "R,4,L,4,L,10,L,10\n"
        video = "n\n"

        inp.extend([ord(c) for c in main_routine])
        inp.extend([ord(c) for c in A])
        inp.extend([ord(c) for c in B])
        inp.extend([ord(c) for c in C])
        inp.extend([ord(c) for c in video])


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
