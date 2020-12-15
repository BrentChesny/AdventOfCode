import re

regex = re.compile("mem\[(\d+)\] = (\d+)")


def parse_input():
    lines = open("input.txt").read().splitlines()
    instructions = []
    current_mask = None
    for line in lines:
        if "mask" in line:
            current_mask = line.strip("mask = ")
        else:
            addr, val = regex.match(line).groups()
            instructions.append((current_mask, int(addr), int(val)))
    return instructions


def mask_value(mask, val):
    v = 0
    b = 0
    for m in reversed(mask):
        if m == "X":
            v += (2 ** b) if val & (2 ** b) else 0
        elif m == "1":
            v += 2 ** b
        b += 1
    return v


def mask_addr(mask, addr):
    addr = format(addr, "036b")
    return "".join(a if m == "0" else m for m, a in zip(mask, addr))


def replace_floating(addrs):
    result = set()
    for addr in addrs:
        result.add(addr.replace("X", "0", 1))
        result.add(addr.replace("X", "1", 1))
    return result


def solve_part_one():
    mem = dict()
    for mask, addr, val in parse_input():
        mem[addr] = mask_value(mask, val)
    return sum(v for v in mem.values())


def solve_part_two():
    mem = dict()
    for mask, addr, val in parse_input():
        masked_addr = mask_addr(mask, addr)
        n_floating = masked_addr.count("X")

        addrs = {masked_addr}
        for _ in range(n_floating):
            addrs = replace_floating(
                addrs,
            )

        for a in addrs:
            mem[a] = val
    return sum(v for v in mem.values())


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
