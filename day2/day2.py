from Input import Input
from typing import List

def part2(input):

    for noun in range(100):
        for verb in range(100):
            if part1(input.copy(), noun, verb) == 19690720:
                # print((noun * 100) + verb)
                return ((noun * 100) + verb)

    return -1


def op_add(input, i_pointer):
    parameter_1 = input[i_pointer + 1]
    parameter_2 = input[i_pointer + 2]
    parameter_3 = input[i_pointer + 3]

    operand_1 = input[parameter_1]
    operand_2 = input[parameter_2]

    input[parameter_3] = operand_1 + operand_2

    return 4


def op_mult(input, i_pointer):
    parameter_1 = input[i_pointer + 1]
    parameter_2 = input[i_pointer + 2]
    parameter_3 = input[i_pointer + 3]

    operand_1 = input[parameter_1]
    operand_2 = input[parameter_2]

    input[parameter_3] = operand_1 * operand_2

    return 4


def part1(input: List[str], noun = -1, verb = -1):

    if noun != -1: input[1] = noun
    if verb != -1: input[2] = verb

    i_pointer = 0
    input_len = len(input)
    while i_pointer < input_len:
        opcode = input[i_pointer]

        if opcode == 99:
            break

        if opcode == 1:
            pointer_shift = op_add(input, i_pointer)
        if opcode == 2:
            pointer_shift = op_mult(input, i_pointer)

        i_pointer += pointer_shift


    return(input[0])

if __name__ == '__main__':
    input = Input(2).lines()
    input = [int(string) for string in input[0].split(',')]

    test = ['1,1,1,4,99,5,6,0,99']
    test = [int(string) for string in test[0].split(',')]

    assert part1(test) == 30

    erg1 = part1(input.copy(), 12, 2)
    print(f'Part 1: {erg1}')

    erg2 = part2(input)
    print(f'Part 2: {erg2}')