from Input import Input
from typing import List



def op_add(input, i_pointer):

    op = input[i_pointer]

    parameter_1 = input[i_pointer + 1] if ( op // 100) % 10 == 0 else i_pointer + 1
    parameter_2 = input[i_pointer + 2] if ( op // 1000) % 10 == 0 else i_pointer + 2
    parameter_3 = input[i_pointer + 3] if ( op // 10000) % 10 == 0 else i_pointer + 3

    operand_1 = input[parameter_1]
    operand_2 = input[parameter_2]

    input[parameter_3] = operand_1 + operand_2

    return 4


def op_mult(input, i_pointer):
    op = input[i_pointer]

    parameter_1 = input[i_pointer + 1] if ( op // 100) % 10 == 0 else i_pointer + 1
    parameter_2 = input[i_pointer + 2] if ( op // 1000) % 10 == 0 else i_pointer + 2
    parameter_3 = input[i_pointer + 3] if ( op // 10000) % 10 == 0 else i_pointer + 3

    operand_1 = input[parameter_1]
    operand_2 = input[parameter_2]

    input[parameter_3] = operand_1 * operand_2

    return 4

def op_input(program, i_pointer):
    op = program[i_pointer]

    parameter_1 = program[i_pointer + 1] if ( op // 100) % 10 == 0 else i_pointer + 1

    program[parameter_1] = input_value

    return 2

def op_output(program, i_pointer):
    op = program[i_pointer]

    parameter_1 = program[i_pointer + 1] if ( op // 100) % 10 == 0 else i_pointer + 1

    print(f'Output {program[parameter_1]}')

    return 2

def op_jmp_if_true(program, i_pointer):
    op = program[i_pointer]

    parameter_1 = program[i_pointer + 1] if ( op // 100) % 10 == 0 else i_pointer + 1
    parameter_2 = program[i_pointer + 2] if ( op // 1000) % 10 == 0 else i_pointer + 2

    parameter_1 = program[parameter_1]
    parameter_2 = program[parameter_2]

    if parameter_1 != 0:
        return parameter_2 - i_pointer
    else:
        return 3


def op_jmp_if_false(program, i_pointer):
    op = program[i_pointer]

    parameter_1 = program[i_pointer + 1] if (op // 100) % 10 == 0 else i_pointer + 1
    parameter_2 = program[i_pointer + 2] if (op // 1000) % 10 == 0 else i_pointer + 2

    parameter_1 = program[parameter_1]
    parameter_2 = program[parameter_2]

    if parameter_1 == 0:
        return parameter_2 - i_pointer
    else:
        return 3

def op_less_than(program, i_pointer):
    op = program[i_pointer]

    parameter_1 = program[i_pointer + 1] if (op // 100) % 10 == 0 else i_pointer + 1
    parameter_2 = program[i_pointer + 2] if (op // 1000) % 10 == 0 else i_pointer + 2
    parameter_3 = program[i_pointer + 3] if (op // 10000) % 10 == 0 else i_pointer + 3

    parameter_1 = program[parameter_1]
    parameter_2 = program[parameter_2]

    if parameter_1 < parameter_2:
        program[parameter_3] = 1
    else:
        program[parameter_3] = 0

    return 4

def op_equals(program, i_pointer):
    op = program[i_pointer]

    parameter_1 = program[i_pointer + 1] if (op // 100) % 10 == 0 else i_pointer + 1
    parameter_2 = program[i_pointer + 2] if (op // 1000) % 10 == 0 else i_pointer + 2
    parameter_3 = program[i_pointer + 3] if (op // 10000) % 10 == 0 else i_pointer + 3

    parameter_1 = program[parameter_1]
    parameter_2 = program[parameter_2]

    if parameter_1 == parameter_2:
        program[parameter_3] = 1
    else:
        program[parameter_3] = 0

    return 4

def program(input: List[int], noun = -1, verb = -1):

    if noun != -1: input[1] = noun
    if verb != -1: input[2] = verb

    i_pointer = 0
    input_len = len(input)
    while i_pointer < input_len:
        opcode = input[i_pointer] % 100

        if opcode == 99:
            break

        if opcode == 1:
            pointer_shift = op_add(input, i_pointer)
        if opcode == 2:
            pointer_shift = op_mult(input, i_pointer)
        if opcode == 3:
            pointer_shift = op_input(input, i_pointer)
        if opcode == 4:
            pointer_shift = op_output(input, i_pointer)
        if opcode == 5:
            pointer_shift = op_jmp_if_true(input, i_pointer)
        if opcode == 6:
            pointer_shift = op_jmp_if_false(input, i_pointer)
        if opcode == 7:
            pointer_shift = op_less_than(input, i_pointer)
        if opcode == 8:
            pointer_shift = op_equals(input, i_pointer)

        i_pointer += pointer_shift


    return(input[0])

if __name__ == '__main__':
    input = Input(5).lines()
    input = [int(string) for string in input[0].split(',')]

    input_value = 1
    program(input.copy())

    print(f'Part 2:')
    input_value = 5
    program(input.copy())