from math import prod

hex_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def parse_input():
    return "".join(hex_map[c] for c in open("input.txt").read().strip())


def bits_to_num(bits):
    return int(bits, 2)


def parse_packet(bits):
    version, bits = bits_to_num(bits[:3]), bits[3:]
    packet_type, bits = bits_to_num(bits[:3]), bits[3:]
    if packet_type == 4:
        stop = False
        n_bits = ""
        while not stop:
            part, bits = bits[:5], bits[5:]
            if part[0] == "0":
                stop = True
            n_bits += part[1:]
        n = bits_to_num(n_bits)
        return (packet_type, version, n, []), bits
    else:
        subpackets, bits = parse_subpackets(bits)
        return (packet_type, version, None, subpackets), bits


def parse_subpackets(bits):
    length_type, bits = bits[0], bits[1:]
    subpacket_length = None
    subpacket_num = None
    if length_type == "0":
        subpacket_length, bits = bits_to_num(bits[:15]), bits[15:]
    else:
        subpacket_num, bits = bits_to_num(bits[:11]), bits[11:]
    subpackets_remaining = True
    bits_processed = 0
    subpackets = []
    while subpackets_remaining:
        bits_before = len(bits)
        subpacket, bits = parse_packet(bits)
        subpackets.append(subpacket)
        bits_after = len(bits)
        bits_processed += bits_before - bits_after
        if (subpacket_length and bits_processed >= subpacket_length) or (
            subpacket_num and len(subpackets) >= subpacket_num
        ):
            subpackets_remaining = False
    return subpackets, bits


def version_sum(packet):
    return packet[1] + sum(version_sum(subpacket) for subpacket in packet[3])


def solve_part_one():
    bits = parse_input()
    packet_root, _ = parse_packet(bits)
    return version_sum(packet_root)


def calculate(packet):
    if packet[0] == 0:
        return sum(calculate(p) for p in packet[3])
    elif packet[0] == 1:
        return prod(calculate(p) for p in packet[3])
    elif packet[0] == 2:
        return min(calculate(p) for p in packet[3])
    elif packet[0] == 3:
        return max(calculate(p) for p in packet[3])
    elif packet[0] == 4:
        return packet[2]
    elif packet[0] == 5:
        return 1 if calculate(packet[3][0]) > calculate(packet[3][1]) else 0
    elif packet[0] == 6:
        return 1 if calculate(packet[3][0]) < calculate(packet[3][1]) else 0
    elif packet[0] == 7:
        return 1 if calculate(packet[3][0]) == calculate(packet[3][1]) else 0


def solve_part_two():
    bits = parse_input()
    packet_root, _ = parse_packet(bits)
    return calculate(packet_root)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
