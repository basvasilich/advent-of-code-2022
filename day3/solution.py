# https://adventofcode.com/2022/day/3
import os
import string


def get_priorities_sum(items: list[str]) -> int:
    result = 0
    for item in items:
        if item != '':
            result += string.ascii_letters.index(item) + 1
    return result


def find_letter_in_line(line: str) -> str:
    s_l = set()
    s_r = set()
    p_l = 0
    p_r = len(line) - 1

    while p_l < (len(line) // 2):
        c_l = line[p_l]
        c_r = line[p_r]
        s_l.add(c_l)
        s_r.add(c_r)
        if c_r in s_l:
            return c_r
        if c_l in s_r:
            return c_l
        p_l += 1
        p_r -= 1

    return ''


def find_letter_in_group(group: list[str]) -> str:
    [line1, line2, line3] = group
    p_1 = len(line1) - 1
    p_2 = len(line2) - 1
    p_3 = len(line3) - 1

    s_1 = set()
    s_2 = set()
    s_3 = set()

    while p_1 or p_2 or p_3:
        if p_1 >= 0:
            c_1 = line1[p_1]
            s_1.add(c_1)
            if c_1 in s_1 and c_1 in s_2 and c_1 in s_3:
                return c_1
            p_1 -= 1
        if p_2 >= 0:
            c_2 = line2[p_2]
            s_2.add(c_2)
            if c_2 in s_1 and c_2 in s_2 and c_2 in s_3:
                return c_2
            p_2 -= 1
        if p_3 >= 0:
            c_3 = line3[p_3]
            s_3.add(c_3)
            if c_3 in s_1 and c_3 in s_2 and c_3 in s_3:
                return c_3
            p_3 -= 1

    return ''


def solution_part1(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    letters = []

    for raw_line in raw_lines:
        letters.append(find_letter_in_line(raw_line.rstrip()))

    return get_priorities_sum(letters)


def solution_part2(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    letters = []

    count = 0
    group = []
    for raw_line in raw_lines:
        group.append(raw_line.rstrip())
        count += 1
        if count == 3:
            letters.append(find_letter_in_group(group))
            count = 0
            group = []

    return get_priorities_sum(letters)


assert (solution_part1('input.test.txt') == 157)
print('Result Part 1: ', solution_part1('input.txt'))
assert (solution_part2('input.test.txt') == 70)
print('Result Part 2: ', solution_part2('input.txt'))
