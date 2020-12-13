from intcode import IntCodeProcessor
from itertools import chain, combinations


def parse_input():
    return list(map(int, open("input.txt").readline().split(",")))


def parse_droid_output(output):
    return "".join([chr(c) for c in output])


def parse_items(output):
    lines = output.split("\n")
    items = []
    for line in lines:
        if len(line) < 2:
            continue
        if line[0] == "-":
            items.append(line[2:])
    return items


def drop_cmd(item):
    return [ord(c) for c in "drop " + item] + [10]


def take_cmd(item):
    return [ord(c) for c in "take " + item] + [10]


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def construct_cmds_for_auto(items):
    cmds = []
    drop_all = []
    for items_to_try in powerset(items):
        for item in items:
            cmds.append(drop_cmd(item))
        for item in items_to_try:
            cmds.append(take_cmd(item))
        cmds.append([ord(c) for c in "north"] + [10])
    return cmds


def main():
    program = parse_input()
    droid = IntCodeProcessor(program, [])
    items = []
    cmds = []
    while not droid.is_halted():
        output = parse_droid_output(droid.execute())
        print(output)
        if "Items in your" in output:
            items = parse_items(output)
        if "Command?" in output:
            print(len(droid.input), len(cmds))
            if cmds:
                cmd, cmds = cmds[0], cmds[1:]
                droid.input.extend(cmd)
            else:
                cmd = input()
                if cmd == "auto":
                    cmds = construct_cmds_for_auto(items)
                    cmd, cmds = cmds[0], cmds[1:]
                    droid.input.extend(cmd)
                else:
                    droid.input.extend([ord(c) for c in cmd])
                    droid.input.append(10)


if __name__ == "__main__":
    main()
