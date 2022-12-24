# https://adventofcode.com2022/day/11
from heapq import heappush, nlargest

test_monkeys = [
    [[79, 98], lambda x: x * 19, [23, 2, 3], 0],
    [[54, 65, 75, 74], lambda x: x + 6, [19, 2, 0], 0],
    [[79, 60, 97], lambda x: x * x, [13, 1, 3], 0],
    [[74], lambda x: x + 3, [17, 0, 1], 0]
]

input_monkeys = [
    [[98, 97, 98, 55, 56, 72], lambda x: x * 13, [11, 4, 7], 0],
    [[73, 99, 55, 54, 88, 50, 55], lambda x: x + 4, [17, 2, 6], 0],
    [[67, 98], lambda x: x * 11, [5, 6, 5], 0],
    [[82, 91, 92, 53, 99], lambda x: x + 8, [13, 1, 2], 0],
    [[52, 62, 94, 96, 52, 87, 53, 60], lambda x: x * x, [19, 3, 1], 0],
    [[94, 80, 84, 79], lambda x: x + 5, [2, 7, 0], 0],
    [[89], lambda x: x + 1, [3, 0, 5], 0],
    [[70, 59, 63], lambda x: x + 3, [7, 4, 3], 0],
]


def solution_part1(monkeys) -> int:
    r = 0
    while r < 20:
        r += 1
        for monkey in monkeys:
            items, fn, logic, count = monkey
            [d, t, f] = logic
            for item in items:
                item = fn(item) // 3
                if item % d == 0:
                    monkeys[t][0].append(item)
                else:
                    monkeys[f][0].append(item)

                monkey[3] += 1

            monkey[0] = []

    h = []
    for monkey in monkeys:
        heappush(h, monkey[3])
    result = nlargest(2, h)

    return result[0] * result[1]


def solution_part2(monkeys) -> int:
    r = 0
    while r < 10000:
        r += 1
        for monkey in monkeys:
            items, fn, logic, count = monkey
            [d, t, f] = logic
            for item in items:
                item = fn(item)
                if item % d == 0:
                    monkeys[t][0].append(item)
                else:
                    monkeys[f][0].append(item)

                monkey[3] += 1

            monkey[0] = []

    h = []
    for monkey in monkeys:
        heappush(h, monkey[3])
    result = nlargest(2, h)

    return result[0] * result[1]


assert (solution_part1(test_monkeys) == 10605)
print('Result Part 1: ', solution_part1(input_monkeys))
# assert (solution_part2(test_monkeys) == 2713310158)
# print('Result Part 2: ', solution_part2(input_monkeys))
