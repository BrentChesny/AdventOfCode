def parse_input():
    particles = []
    for line in open('input.txt').readlines():
        parts = line.strip().split(', ')
        particle = map(parse_vector, parts)
        particles.append(particle)
    return particles

def solve_part_one():
    particles = parse_input()
    closest = None

    for _ in xrange(1000):
        closestDist = None

        for i, particle in enumerate(particles):
            particle[1] = (particle[1][0] + particle[2][0], particle[1][1] + particle[2][1], particle[1][2] + particle[2][2])
            particle[0] = (particle[0][0] + particle[1][0], particle[0][1] + particle[1][1], particle[0][2] + particle[1][2])

            dist = sum(map(abs, particle[0]))
            if closestDist == None or dist < closestDist:
                closestDist = dist
                closest = i

    return closest

def solve_part_two():
    particles = parse_input()
    destroyed = set()

    for _ in xrange(100):
        for i, particle in enumerate(particles):
            if i in destroyed:
                continue
            particle[1] = (particle[1][0] + particle[2][0], particle[1][1] + particle[2][1], particle[1][2] + particle[2][2])
            particle[0] = (particle[0][0] + particle[1][0], particle[0][1] + particle[1][1], particle[0][2] + particle[1][2])

        destroy = []
        for i, p1 in enumerate(particles):
            for j, p2 in enumerate(particles):
                if i != j and p1[0] == p2[0] and p1 not in destroy:
                    destroy.append(p1)

        for p in destroy:
            particles.remove(p)

    return len(particles)

def parse_vector(string):
    return tuple(map(int, string[3:-1].split(',')))

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
