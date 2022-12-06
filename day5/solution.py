# https://adventofcode.com/2022/day/5
import os
from typing import NewType

StackT = NewType('StackT', list[str])
MoveT = NewType('MoveT', tuple[str, int, int])


def get_input(filename) -> (list[StackT], list[MoveT]):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    stacks = []
    moves = []
    s_end = 0

    if len(raw_lines) == 0:
        return stacks, moves

    for index, line in enumerate(raw_lines):
        if 'from' in line:
            [action, volume, _, from_s, _, to_s] = line.rstrip().split(' ')
            moves.append((action, volume, from_s, to_s))
        elif '1' in line:
            last_s = int(line.rstrip().split(' ').pop())
            stacks = [[] for _ in range(last_s)]
            s_end = index

    for i in range(s_end):
        line = raw_lines[i]
        letters = line[1::4]
        for j, char in enumerate(letters):
            if char != ' ':
                stacks[j].append(char)

    return [list(reversed(x)) for x in stacks], moves


def make_s_tmp(stacks: list[StackT], vol: str, s_from_i: str) -> list[str]:
    s_from = stacks[int(s_from_i) - 1]
    s_tmp = []
    i = int(vol)
    while i:
        item = s_from.pop()
        s_tmp.append(item)
        i -= 1
    return s_tmp


def make_result(stacks: list[StackT]) -> str:
    result = ''

    for i in range(len(stacks)):
        result += stacks[i].pop()

    return result


def solution_part1(filename: str) -> str:
    stacks, moves = get_input(filename)
    for action, vol, s_from_i, s_to_i in moves:
        if action == 'move':
            s_to = stacks[int(s_to_i) - 1]
            s_to += make_s_tmp(stacks, vol, s_from_i)

    return make_result(stacks)


def solution_part2(filename: str) -> str:
    stacks, moves = get_input(filename)
    for action, vol, s_from_i, s_to_i in moves:
        if action == 'move':
            s_to = stacks[int(s_to_i) - 1]
            s_tmp = make_s_tmp(stacks, vol, s_from_i)
            i = int(vol)
            while i:
                item = s_tmp.pop()
                s_to.append(item)
                i -= 1

    return make_result(stacks)


assert (solution_part1('input.test.txt') == 'CMZ')
print('Result Part 1: ', solution_part1('input.txt'))
assert (solution_part2('input.test.txt') == 'MCD')
print('Result Part 2: ', solution_part2('input.txt'))
