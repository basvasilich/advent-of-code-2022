# https://adventofcode.com/2022/day/2
import os


def get_line_score_part1(opp: str, you: str) -> int:
    if opp == 'A':
        if you == 'X':
            return 3 + 1
        if you == 'Y':
            return 6 + 2
        if you == 'Z':
            return 0 + 3
    if opp == 'B':
        if you == 'X':
            return 0 + 1
        if you == 'Y':
            return 3 + 2
        if you == 'Z':
            return 6 + 3
    if opp == 'C':
        if you == 'X':
            return 6 + 1
        if you == 'Y':
            return 0 + 2
        if you == 'Z':
            return 3 + 3


def get_line_score_part2(opp: str, you: str) -> int:
    if opp == 'A':
        if you == 'X':
            return 0 + 3
        if you == 'Y':
            return 3 + 1
        if you == 'Z':
            return 6 + 2

    if opp == 'B':
        if you == 'X':
            return 0 + 1
        if you == 'Y':
            return 3 + 2
        if you == 'Z':
            return 6 + 3
    if opp == 'C':
        if you == 'X':
            return 0 + 2
        if you == 'Y':
            return 3 + 3
        if you == 'Z':
            return 6 + 1


def solution_part2(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    total_score = 0

    for raw_line in raw_lines:
        [a, b] = raw_line.rstrip().split(' ')
        total_score += get_line_score_part2(a, b)

    return total_score


def solution_part1(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    total_score = 0

    for raw_line in raw_lines:
        [a, b] = raw_line.rstrip().split(' ')
        total_score += get_line_score_part1(a, b)

    return total_score


assert (solution_part1('input.test.txt') == 15)
print('Result Part 1: ', solution_part1('input1.txt'))
assert (solution_part2('input.test.txt') == 12)
print('Result Part 2: ', solution_part2('input1.txt'))
