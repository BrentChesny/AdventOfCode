def parse_input():
    return list(map(int, open('input.txt').read().strip().split(' ')))

def parse_tree(serialized_tree):
    n_children = serialized_tree.pop(0)
    n_meta = serialized_tree.pop(0)

    children = []
    for _ in range(n_children):
        children.append(parse_tree(serialized_tree))

    meta = []
    for _ in range(n_meta):
        meta.append(serialized_tree.pop(0))

    return (children, meta)

def sum_metas(tree):
    return sum(sum_metas(child) for child in tree[0]) + sum(tree[1])

def node_value(node):
    children, metas = node
    if not children:
        return sum(metas)
    else:
        value = 0
        for meta in metas:
            if meta == 0 or meta > len(children):
                continue
            else:
                value += node_value(children[meta-1])
        return value

def solve_part_one():
    tree = parse_tree(parse_input())
    return sum_metas(tree)


def solve_part_two():
    tree = parse_tree(parse_input())
    return node_value(tree)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
