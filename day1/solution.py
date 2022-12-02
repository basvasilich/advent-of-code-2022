# https://adventofcode.com/2022/day/1
import os
from heapq import heappush, nlargest


def solution_part1(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    max_result = 0
    cur_sum = 0

    for raw_line in raw_lines:
        if raw_line.rstrip() == '':
            max_result = max(max_result, cur_sum)
            cur_sum = 0
        else:
            cur_sum += int(raw_line.rstrip())

    max_result = max(max_result, cur_sum)

    return max_result


def solution_part2(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    h = []
    cur_sum = 0

    for raw_line in raw_lines:
        if raw_line.rstrip() == '':
            heappush(h, cur_sum)
            cur_sum = 0
        else:
            cur_sum += int(raw_line.rstrip())

    heappush(h, cur_sum)

    return sum(nlargest(3, h))


assert (solution_part1('input.test.txt') == 24000)
print('Result Part 1: ', solution_part1('input1.txt'))
assert (solution_part2('input.test.txt') == 45000)
print('Result Part 2: ', solution_part2('input1.txt'))
