def parse_input():
    components = set()
    for line in open('input.txt').readlines():
        components.add(tuple(map(int, line.strip().split('/'))))
    return components

def solve_part_one():
    components = parse_input()
    strengths = []

    def search(bridge, components):
        end_of_bridge = True
        for comp in components:
            if bridge[-1] in comp:
                new_components = set(components)
                new_components.remove(comp)
                end_of_bridge = False
                if comp[0] == bridge[-1]:
                    search(bridge + list(comp), new_components)
                elif comp[1] == bridge[-1]:
                    search(bridge + list(reversed(comp)), new_components)
        if end_of_bridge:
            strengths.append(sum(bridge))

    search([0], components)
    return max(strengths)

def solve_part_two():
    components = parse_input()
    strengths = []

    def search(bridge, components):
        end_of_bridge = True
        for comp in components:
            if bridge[-1] in comp:
                new_components = set(components)
                new_components.remove(comp)
                end_of_bridge = False
                if comp[0] == bridge[-1]:
                    search(bridge + list(comp), new_components)
                elif comp[1] == bridge[-1]:
                    search(bridge + list(reversed(comp)), new_components)
        if end_of_bridge:
            strengths.append((len(bridge), sum(bridge)))

    search([0], components)
    return max(strengths)[1]


def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
