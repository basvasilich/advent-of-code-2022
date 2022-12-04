# https://adventofcode.com/2022/day/4
import os
from heapq import heappush, heappop


def get_pairs(line: str) -> list[list[int]]:
    result = []
    elf_pairs = line.rstrip().split(',')
    for elf_pair in elf_pairs:
        result.append([int(y) for y in elf_pair.split('-')])
    return result


def solution_part1(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    result = 0

    for line in raw_lines:
        [e1, e2] = get_pairs(line)

        if (e1[0] <= e2[0] and e1[1] >= e2[1]) or (e2[0] <= e1[0] and e2[1] >= e1[1]):
            result += 1

    return result


def solution_part2(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    result = 0

    for line in raw_lines:
        [e1, e2] = get_pairs(line)
        timeline = []
        heappush(timeline, (e1[0], 'e1'))
        heappush(timeline, (e1[1], 'e1'))
        heappush(timeline, (e2[0], 'e2'))
        heappush(timeline, (e2[1], 'e2'))

        s = [heappop(timeline)]
        last_s = s[0]
        while len(timeline):
            (point, elf) = heappop(timeline)

            if len(s):
                (last_point, last_elf) = s.pop()
                if last_elf == elf:
                    last_s = (point, elf)
                else:
                    result += 1
                    break
            elif point == last_s[0] and last_s[1] != elf:
                result += 1
                break
            else:
                s.append((point, elf))

    return result


assert (solution_part1('input.test.txt') == 2)
print('Result Part 1: ', solution_part1('input.txt'))
assert (solution_part2('input.test.txt') == 4)
print('Result Part 2: ', solution_part2('input.txt'))
