from Input import Input
from typing import List
from collections import defaultdict

def part2(input):
    tokens = []
    for line in input:
        line = [(token[0], token[1:]) for token in line.split(',')]
        tokens.append(line)


    dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    dy = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

    point_lists = []

    for tokenline in tokens:
        x = 0
        y = 0
        points = defaultdict(int)
        length = 0
        for token in tokenline:
            dir = token[0]
            size = int(token[1])
            for _ in range(size):
                x += dx[dir]
                y += dy[dir]
                length += 1
                points[(x,y)] += length
        point_lists.append(points)

    intersection = set(point_lists[0].keys()) & set(point_lists[1].keys())
    min_dist = min([point_lists[0][(x,y)] + point_lists[1][(x,y)] for (x,y) in intersection])
    print(intersection)
    print(min_dist)

    return min_dist

def part1(input):
    tokens = []
    for line in input:
        line = [(token[0], token[1:]) for token in line.split(',')]
        tokens.append(line)

    dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    dy = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

    point_lists = []

    for tokenline in tokens:
        x = 0
        y = 0
        points = set()
        for token in tokenline:
            dir = token[0]
            size = int(token[1])
            for _ in range(size):
                x += dx[dir]
                y += dy[dir]
                points.add((x,y))
        point_lists.append(points)

    intersection = point_lists[0] & point_lists[1]
    min_dist = min([abs(x) + abs(y) for (x,y) in intersection])
    print(intersection)
    print(min_dist)

    return min_dist



if __name__ == '__main__':
    input = Input(3).lines()

    test1 = ["R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83"]
    test2= ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]

    assert part1(test1) == 159
    assert part1(test2) == 135

    erg = part1(input)

    assert part2(test1) == 610
    assert part2(test2) == 410

    erg2 = part2(input)

