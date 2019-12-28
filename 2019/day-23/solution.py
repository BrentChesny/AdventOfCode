from intcode import IntCodeProcessor
from collections import defaultdict


def parse_input():
    return list(map(int, open('input.txt').readline().split(',')))


def solve_part_one():
    program = parse_input()
    inputs = [[addr] for addr in range(50)]
    packet_queue = defaultdict(list)
    network = [IntCodeProcessor(program, i) for i in inputs]

    while not packet_queue[255]:
        for addr, computer in enumerate(network):
            output = computer.execute()

            while output:
                packet, output = output[:3], output[3:]
                to, x, y = packet
                packet_queue[to].append((x, y))

            if len(packet_queue[addr]):
                x, y = packet_queue[addr].pop(0)
                computer.input.extend([x, y])
            else:
                computer.input.append(-1)

    _, y = packet_queue[255].pop(0)
    return y


def solve_part_two():
    program = parse_input()
    inputs = [[addr] for addr in range(50)]
    packet_queue = defaultdict(list)
    network = [IntCodeProcessor(program, i) for i in inputs]
    last_nat_y = None

    idle_rounds = 0
    while True:
        all_idle = True
        for addr, computer in enumerate(network):
            output = computer.execute()

            while output:
                packet, output = output[:3], output[3:]
                to, x, y = packet
                packet_queue[to].append((x, y))
                all_idle = False

            if len(packet_queue[addr]):
                x, y = packet_queue[addr].pop(0)
                computer.input.extend([x, y])
                all_idle = False
            else:
                computer.input.append(-1)

        if all_idle:
            idle_rounds += 1
        else:
            idle_rounds = 0

        if idle_rounds == 5:
            x, y = packet_queue[255][-1]
            network[0].input.extend([x, y])
            if y == last_nat_y:
                return y
            last_nat_y = y


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
