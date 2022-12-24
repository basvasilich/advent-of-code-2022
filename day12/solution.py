# https://adventofcode.com/2022/day/8
import os
import string
from queue import Queue


def get_input(filename) -> (list[list[int, int]], (int, int), (int, int)):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return []

    board = []
    s = 0, 0
    e = 0, 0
    p_s = set()

    for row, line in enumerate(raw_lines):
        board.append([])
        lst = list(line.rstrip())

        for col, char in enumerate(lst):
            if char == 'S':
                s = row, col
                p_s.add(s)
                board[row].append(0)
            elif char == 'E':
                e = row, col
                board[row].append(string.ascii_lowercase.find('z'))
            else:
                if char == 'a':
                    p_s.add((row, col))
                board[row].append(string.ascii_lowercase.find(char))

    return board, s, e, p_s


def helper(board, s, e):
    visited = set()
    in_q = set()

    q = Queue()
    q.put_nowait((s[0], s[1], 0))
    in_q.add((s[0], s[1]))

    while not q.empty():
        row, col, dst = q.get_nowait()
        visited.add((row, col))
        h = board[row][col]
        if (row, col) == e:
            return dst
        else:
            if row > 0:
                n_h = board[row - 1][col]
                if n_h - h < 2 and (row - 1, col) not in visited and (row - 1, col) not in in_q:
                    q.put_nowait((row - 1, col, dst + 1))
                    in_q.add((row - 1, col))
            if row < len(board) - 1:
                n_h = board[row + 1][col]
                if n_h - h < 2 and (row + 1, col) not in visited and (row + 1, col) not in in_q:
                    q.put_nowait((row + 1, col, dst + 1))
                    in_q.add((row + 1, col))
            if col > 0:
                n_h = board[row][col - 1]
                if n_h - h < 2 and (row, col - 1) not in visited and (row, col - 1) not in in_q:
                    q.put_nowait((row, col - 1, dst + 1))
                    in_q.add((row, col - 1))
            if col < len(board[0]) - 1:
                n_h = board[row][col + 1]
                if n_h - h < 2 and (row, col + 1) not in visited and (row, col + 1) not in in_q:
                    q.put_nowait((row, col + 1, dst + 1))
                    in_q.add((row, col + 1))

    return len(board) * len(board[0]) * 10


def solution_part1(filename: str) -> (int, set[(int, int)], list[list[int]]):
    board, s, e, _ = get_input(filename)
    return helper(board, s, e)


def solution_part2(filename: str) -> (int, set[(int, int)], list[list[int]]):
    board, _, e, p_s = get_input(filename)

    min_result = len(board) * len(board[0]) * 10

    for start in p_s:
        min_result = min(min_result, helper(board, start, e))
    return min_result


assert (solution_part1('input.test.txt') == 31)
print('Result Part 1: ', solution_part1('input.txt'))
assert (solution_part2('input.test.txt') == 29)
print('Result Part 2: ', solution_part2('input.txt'))
