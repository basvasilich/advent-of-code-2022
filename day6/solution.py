# https://adventofcode.com/2022/day/4
import os


def find_seq_index_by_length(line: str, n: int):
    pointer_start = 0
    pointer_end = 0
    window_counter = {}

    while pointer_end < len(line):
        if pointer_end - pointer_start < n:
            char_end = line[pointer_end]

            if char_end in window_counter:
                window_counter[char_end] += 1
            else:
                window_counter[char_end] = 1

        else:
            char_end = line[pointer_end]

            if char_end in window_counter:
                window_counter[char_end] += 1
            else:
                window_counter[char_end] = 1

            char_start = line[pointer_start]

            if char_start in window_counter and window_counter[char_start] == 1:
                window_counter.pop(char_start, None)
            else:
                window_counter[char_start] -= 1

            pointer_start += 1

        pointer_end += 1

        if len(window_counter) == n:
            return pointer_end

    return -1


def solution_part1(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        line = raw_lines[0]

    return find_seq_index_by_length(line, 4)


def solution_part2(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        line = raw_lines[0]

    return find_seq_index_by_length(line, 14)


assert (solution_part1('input1.test.txt') == 7)
assert (solution_part1('input2.test.txt') == 5)
assert (solution_part1('input3.test.txt') == 6)
assert (solution_part1('input4.test.txt') == 10)
assert (solution_part1('input5.test.txt') == 11)
print('Result Part 1: ', solution_part1('input.txt'))
assert (solution_part2('input1.test.txt') == 19)
assert (solution_part2('input2.test.txt') == 23)
assert (solution_part2('input3.test.txt') == 23)
assert (solution_part2('input4.test.txt') == 29)
assert (solution_part2('input5.test.txt') == 26)
print('Result Part 2: ', solution_part2('input.txt'))
