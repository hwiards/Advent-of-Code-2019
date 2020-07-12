from Input import Input
from typing import List
from collections import Counter

def is_valid(number_: str):
    is_monotonic = list(number_) == sorted(number_)
    if not is_monotonic:
        return False

    has_double = max(Counter(number_).values()) > 1
    return has_double

def is_valid2(number_: str):
    is_monotonic = list(number_) == sorted(number_)
    if not is_monotonic:
        return False

    has_exact_double = 2 in Counter(number_).values()
    return has_exact_double

# def calc_next_valid(num: int):
#     num_1 = num + 1
#     as_str = list(str(num_1))
#     for idx, (c0, c1) in enumerate(zip(as_str[0:], as_str[1:])):
#         # print(idx, c0, c1)
#         if c1 < c0:
#             for i in range(idx+1, len(as_str)):
#                 as_str[i] = c0
#             break
#
#     next_n = int(''.join(as_str))
#     print(next_n)
#     return next_n


def part1(input):

    range_start, range_end = input.split('-')
    range_start, range_end = int(range_start), int(range_end)
    print(range_start, range_end)

    num_valid_pass = 0
    num_valid_pass2 = 0

    for act_num in range(range_start, range_end):
        if is_valid(str(act_num)):
            num_valid_pass += 1
        if is_valid2(str(act_num)):
            num_valid_pass2 += 1

    print(num_valid_pass)
    print(num_valid_pass2)


if __name__ == '__main__':
    input = Input(4).lines()

    part1(input[0])