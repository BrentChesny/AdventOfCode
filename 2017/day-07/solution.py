from collections import Counter

def solve_part_one():
    tree = dict()
    for line in open('input.txt').readlines():
        parts = line.split(' -> ')
        info = parts[0].strip()
        children = parts[1].strip().split(', ') if len(parts) > 1 else []
        name, weight = info.split()
        weight = int(weight[1:-1])
        tree[name] = (weight, children)

    for name in tree:
        found = False
        for _, children in tree.values():
            if name in children:
                found = True
        if found == False:
            return name

def solve_part_two():
    tree = dict()
    for line in open('input.txt').readlines():
        parts = line.split(' -> ')
        info = parts[0].strip()
        children = parts[1].strip().split(', ') if len(parts) > 1 else []
        name, weight = info.split()
        weight = int(weight[1:-1])
        tree[name] = (weight, children)

    _, solution = balance(tree, 'gynfwly')

    return solution

def balance(tree, root):
    weight, children = tree[root]
    solution = None

    children_weights = []
    for child in children:
        w, s = balance(tree, child)
        if not solution:
            solution = s
        children_weights.append(w)

    # If children not balanced...
    if len(set(children_weights)) > 1:
        counter = Counter(children_weights)
        wrong_subtree_weight = min(counter, key=counter.get)
        right_subtree_weight = max(counter, key=counter.get)
        delta = right_subtree_weight - wrong_subtree_weight
        index = children_weights.index(wrong_subtree_weight)
        if not solution:
            solution = tree[children[index]][0] + delta

    return weight + sum(children_weights), solution

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
