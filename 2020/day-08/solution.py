def parse_input():
    return [
        (line.split()[0], int(line.split()[1]))
        for line in open("input.txt").read().splitlines()
    ]


class InfiniteLoopError(Exception):
    def __init__(self, accumulator):
        self.accumulator = accumulator


class Program:
    def __init__(self, code):
        self.code = code
        self.pc = 0
        self.accumulator = 0

    def run(self):
        seen = set()
        while self.pc < len(self.code):
            if self.pc in seen:
                raise InfiniteLoopError(self.accumulator)
            seen.add(self.pc)
            op, arg = self.code[self.pc]
            if op == "acc":
                self.accumulator += arg
            elif op == "jmp":
                self.pc += arg - 1
            elif op == "nop":
                pass
            self.pc += 1
        return self.accumulator


def solve_part_one():
    try:
        Program(parse_input()).run()
    except InfiniteLoopError as e:
        return e.accumulator


def solve_part_two():
    code = parse_input()
    for idx, instr in enumerate(code):
        copy = code[:]
        if instr[0] == "acc":
            continue
        if instr[0] == "jmp":
            copy[idx] = ("nop", instr[1])
        if instr[0] == "nop":
            copy[idx] = ("jmp", instr[1])
        try:
            return Program(copy).run()
        except InfiniteLoopError as e:
            pass


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
