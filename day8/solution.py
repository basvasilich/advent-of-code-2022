# https://adventofcode.com/2022/day/8
import os


def get_input(filename) -> list[list[int]]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    board = []

    if len(raw_lines) == 0:
        return []

    for line in raw_lines:
        board.append([int(x) for x in list(line.rstrip())])

    return board


def solution_part1(filename: str) -> (int, set[(int, int)], list[list[int]]):
    board = get_input(filename)

    visible = set()
    count = 0

    for row in range(len(board)):
        max_l = -1
        p_l = 0
        while p_l < len(board[0]) - 1:
            val_l = board[row][p_l]
            if val_l > max_l:
                if (row, p_l) not in visible:
                    count += 1
                    visible.add((row, p_l))
                max_l = val_l

            p_l += 1

        max_r = -1
        p_r = len(board[0]) - 1
        while p_r > 0:
            val_r = board[row][p_r]
            if val_r > max_r:
                if (row, p_r) not in visible:
                    count += 1
                    visible.add((row, p_r))
                max_r = val_r

            p_r -= 1

    for col in range(len(board[0])):
        max_t = -1
        p_t = 0
        while p_t < len(board) - 1:
            val_t = board[p_t][col]
            if val_t > max_t:
                if (p_t, col) not in visible:
                    count += 1
                    visible.add((p_t, col))
                max_t = val_t

            p_t += 1

        max_b = -1
        p_b = len(board) - 1

        while p_b > 0:
            val_b = board[p_b][col]
            if val_b > max_b:
                if (p_b, col) not in visible:
                    count += 1
                    visible.add((p_b, col))

                max_b = val_b

            p_b -= 1

    return count, visible, board


def solution_part2(filename: str) -> int:
    board = get_input(filename)

    max_result = 0

    for row in range(1, len(board) - 1):
        for col in range(1, len(board[0]) - 1):
            val = board[row][col]

            v_d_t = 1
            v_d_b = 1
            v_d_r = 1
            v_d_l = 1

            cur_t = row - 1
            cur_v = board[cur_t][col]
            while cur_t > 0 and cur_v < val:
                cur_t -= 1
                cur_v = board[cur_t][col]
                v_d_t += 1

            cur_b = row + 1
            cur_v = board[cur_b][col]
            while cur_b < len(board) - 1 and cur_v < val:
                cur_b += 1
                cur_v = board[cur_b][col]
                v_d_b += 1

            cur_r = col + 1
            cur_v = board[row][cur_r]
            while cur_r < len(board[0]) - 1 and cur_v < val:
                cur_r += 1
                cur_v = board[row][cur_r]
                v_d_r += 1

            cur_l = col - 1
            cur_v = board[row][cur_l]
            while cur_l > 0 and cur_v < val:
                cur_l -= 1
                cur_v = board[row][cur_l]
                v_d_l += 1

            max_result = max(v_d_t * v_d_b * v_d_r * v_d_l, max_result)

    return max_result


assert (solution_part1('input.test.txt')[0] == 21)
print('Result Part 1: ', solution_part1('input.txt')[0])
assert (solution_part2('input.test.txt') == 8)
print('Result Part 2: ', solution_part2('input.txt'))
