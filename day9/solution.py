# https://adventofcode.com/2022/day/9
import os


def tail_move(h_coords: (int, int), t_coords: (int, int), v: set[(int, int)], is_tail: bool):
    h_x, h_y = h_coords
    t_x, t_y = t_coords

    if abs(h_x - t_x) < 2 and abs(h_y - t_y) < 2:
        if is_tail:
            v.add(t_coords)
        return t_coords, v

    if t_x == h_x and h_y > t_y:
        t_coords = (t_x, t_y + 1)
    elif t_x == h_x and h_y < t_y:
        t_coords = (t_x, t_y - 1)
    elif t_y == h_y and h_x > t_x:
        t_coords = (t_x + 1, t_y)
    elif t_y == h_y and h_x < t_x:
        t_coords = (t_x - 1, t_y)
    elif h_x > t_x and h_y > t_y:
        t_coords = (t_x + 1, t_y + 1)
    elif h_x > t_x and h_y < t_y:
        t_coords = (t_x + 1, t_y - 1)
    elif h_x < t_x and h_y < t_y:
        t_coords = (t_x - 1, t_y - 1)
    elif h_x < t_x and h_y > t_y:
        t_coords = (t_x - 1, t_y + 1)

    if is_tail:
        v.add(t_coords)

    return t_coords, v


def solution_part1(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    visited = set()

    head_coords = (0, 0)
    tail_coords = (0, 0)

    def head_move(d: str, c: int, h_coords, t_coords, v) -> ((int, int), (int, int), set[(int, int)]):
        while c > 0:
            if d == 'U':
                h_coords = (h_coords[0], h_coords[1] + 1)
            elif d == 'D':
                h_coords = (h_coords[0], h_coords[1] - 1)
            elif d == 'R':
                h_coords = (h_coords[0] + 1, h_coords[1])
            elif d == 'L':
                h_coords = (h_coords[0] - 1, h_coords[1])

            t_coords, v = tail_move(h_coords, t_coords, v, True)
            c -= 1
        return h_coords, t_coords, v

    for line in raw_lines:
        direction, count = line.rstrip().split(' ')
        head_coords, tail_coords, visited = head_move(direction, int(count), head_coords, tail_coords, visited)

    return len(visited)


def solution_part2(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    visited = set()

    knots = [(0, 0) for _ in range(10)]

    for line in raw_lines:
        direction, count = line.rstrip().split(' ')
        c = int(count)

        while c > 0:
            if direction == 'U':
                knots[0] = (knots[0][0], knots[0][1] + 1)
            elif direction == 'D':
                knots[0] = (knots[0][0], knots[0][1] - 1)
            elif direction == 'R':
                knots[0] = (knots[0][0] + 1, knots[0][1])
            elif direction == 'L':
                knots[0] = (knots[0][0] - 1, knots[0][1])

            for i in range(1, len(knots)):
                h_coords = knots[i - 1]
                t_coords = knots[i]
                knots[i], visited = tail_move(h_coords, t_coords, visited, i == 9)
            c -= 1

    return len(visited)


assert (solution_part1('input.test.txt') == 13)
print('Result Part 1: ', solution_part1('input.txt'))
assert (solution_part2('input.test.txt') == 1)
assert (solution_part2('input2.test.txt') == 36)
print('Result Part 2: ', solution_part2('input.txt'))
