from math import floor, ceil


class Node(object):
    def __init__(self, number, parent=None):
        self.parent = parent
        if isinstance(number, list):
            self.value = None
            self.left = Node(number[0], self)
            self.right = Node(number[1], self)
        else:
            self.value = number
            self.left = None
            self.right = None

    def __str__(self) -> str:
        if self.value != None:
            return str(self.value)
        return "[{}, {}]".format(self.left, self.right)


def parse_input():
    return [eval(line.strip()) for line in open("input.txt")]


def traverse(node, depth=0):
    if node.left:
        yield from traverse(node.left, depth + 1)
    yield node, depth
    if node.right:
        yield from traverse(node.right, depth + 1)


def get_root(node):
    while node.parent:
        node = node.parent
    return node


def next_node(node):
    seen = False
    nxt = None
    for n, d in traverse(get_root(node)):
        if n == node:
            seen = True
        if seen and n.value != None and n != node:
            nxt = n
            return nxt


def prev_node(node):
    seen = False
    prv = None
    for n, d in traverse(get_root(node)):
        if n == node:
            seen = True
            return prv
        if not seen and n.value != None:
            prv = n


def explode(node):
    prv, nxt = prev_node(node.left), next_node(node.right)
    if prv:
        prv.value += node.left.value
    if nxt:
        nxt.value += node.right.value
    node.value = 0
    node.left = None
    node.right = None


def split(node):
    l = floor(node.value / 2)
    r = ceil(node.value / 2)
    node.value = None
    node.left = Node(l, node)
    node.right = Node(r, node)


def add(a, b):
    n = Node(0)
    n.value = None
    n.left = a
    n.left.parent = n
    n.right = b
    n.right.parent = n
    return n


def magnitude(node):
    if node.value != None:
        return node.value
    else:
        return 3 * magnitude(node.left) + 2 * magnitude(node.right)


def reduce(node):
    stop = False
    while not stop:
        stop = True
        for n, d in traverse(node):
            if d >= 4 and n.value == None:
                explode(n)
                stop = False
                break
        if not stop:
            continue
        for n, d in traverse(node):
            if n.value and n.value >= 10:
                split(n)
                stop = False
                break
    return node


def solve_part_one():
    numbers = parse_input()
    n = Node(numbers[0])
    for m in numbers[1:]:
        n = reduce(add(n, Node(m)))
    return magnitude(n)


def solve_part_two():
    numbers = parse_input()
    return max(
        magnitude(reduce(add(Node(numbers[i]), Node(numbers[j]))))
        for i in range(len(numbers))
        for j in range(len(numbers))
        if i != j
    )


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
