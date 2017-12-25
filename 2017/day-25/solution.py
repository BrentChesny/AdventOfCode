LEFT = -1
RIGHT = 1

TM = {
    ('A', 0) : (1, RIGHT, 'B'),
    ('A', 1) : (1, LEFT, 'E'),
    ('B', 0) : (1, RIGHT, 'C'),
    ('B', 1) : (1, RIGHT, 'F'),
    ('C', 0) : (1, LEFT, 'D'),
    ('C', 1) : (0, RIGHT, 'B'),
    ('D', 0) : (1, RIGHT, 'E'),
    ('D', 1) : (0, LEFT, 'C'),
    ('E', 0) : (1, LEFT, 'A'),
    ('E', 1) : (0, RIGHT, 'D'),
    ('F', 0) : (1, RIGHT, 'A'),
    ('F', 1) : (1, RIGHT, 'C'),
}

def solve_part_one():
    tape = [0] * int(1e7)
    head = int(1e7)/2
    state = 'A'

    for _ in xrange(12459852):
        write, move, new_state = TM[(state, tape[head])]
        tape[head] = write
        head += move
        state = new_state

    return sum(tape)

def main():
    print 'Part one: ', solve_part_one()

if __name__ == '__main__':
    main()
