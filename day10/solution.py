# https://adventofcode.com/2022/day/10
import os


def solution_part1(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    result = 0
    actions = []

    for line in raw_lines:
        if line.rstrip() == 'noop':
            actions.append(('noop', 0))
        else:
            action, value = line.rstrip().split(' ')
            actions.append((action, int(value)))

    actions = list(reversed(actions))

    timeline = {}

    x = 1
    cycle = 1
    while len(actions):
        action, value = actions.pop()
        if action == 'noop':
            cycle += 1
        elif action == 'addx':
            cycle += 2
            x += value
            timeline[cycle] = x

    x = 1
    cycle = 1
    while cycle < 221:
        if cycle in timeline:
            x = timeline[cycle]

        if cycle == 20:
            result += 20 * x
        elif cycle == 60:
            result += 60 * x
        elif cycle == 100:
            result += 100 * x
        elif cycle == 140:
            result += 140 * x
        elif cycle == 180:
            result += 180 * x
        elif cycle == 220:
            result += 220 * x

        cycle += 1

    return result


assert (solution_part1('input.test.txt') == 13140)
print('Result Part 1: ', solution_part1('input.txt'))
# assert (solution_part2('input.test.txt') == 1)
# print('Result Part 2: ', solution_part2('input.txt'))
