from Input import Input
from typing import List
from collections import defaultdict


def part1(input):
    in_orbit_of_direct = defaultdict(set)

    direct = 0
    indirect = 0
    for line in input:
        center, orbit = line.split(')')
        in_orbit_of_direct[center].add(orbit)
        direct += 1

    new_indir = True
    while new_indir:
        new_indir = False
        for key, value in in_orbit_of_direct.items():
            for item in value:
                for indir in in_orbit_of_direct[item]:
                    if indir not in value:
                        value.add(indir)
                        indirect += 1
                        new_indir = True

    print(direct + indirect)

if __name__ == '__main__':
    # input = Input(6).lines()
    input = Input(6).linesTest()

    part1(input)