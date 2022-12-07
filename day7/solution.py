# https://adventofcode.com/2022/day/7
import os
from heapq import heappop, heappush


class Node:
    def __init__(self, title='', parent=None, vol=0):
        self.children = {}
        self.parent = parent
        self.title = title
        self.vol = vol

    def add_child(self, child):
        self.children[child.title] = child

    def add_vol(self, val):
        self.vol += val


def get_input(filename) -> Node | None:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    root_node = Node('/')
    cur_p = root_node
    if len(raw_lines) == 0:
        return root_node

    counter = 0

    def add_child(s: str, parent: Node):
        [vol, title] = s.split(' ')

        if vol == 'dir':
            parent.add_child(Node(title, parent))
        else:
            parent.add_child(Node(title, parent, int(vol)))
        return parent

    while counter < len(raw_lines):
        line = raw_lines[counter].rstrip()

        if line == '$ cd /':
            cur_p = root_node
        elif '$ cd ..' in line:
            cur_p = cur_p.parent
        elif '$ cd' in line:
            [_, _, title] = line.split(' ')
            cur_p = cur_p.children[title]
        elif '$' not in line:
            cur_p = add_child(line, cur_p)

        counter += 1

    return root_node


def solution_part1(filename: str) -> int:
    tree = get_input(filename)

    def get_vol(root: Node, s: int):
        if bool(root.children):
            for key in root.children.keys():
                node = root.children[key]
                if node.vol:
                    root.add_vol(node.vol)
                else:
                    if bool(node.children):
                        s = get_vol(node, s)
                    root.add_vol(node.vol)

        if root.vol < 100000:
            s += root.vol
        return s

    result = get_vol(tree, 0)

    return result


def solution_part2(filename: str) -> int:
    tree = get_input(filename)

    def get_vol(root: Node, heap):
        if bool(root.children):
            for key in root.children.keys():
                node = root.children[key]
                if node.vol:
                    root.add_vol(node.vol)
                else:
                    if bool(node.children):
                        heap = get_vol(node, heap)
                    root.add_vol(node.vol)
        heappush(heap, root.vol)

        return heap

    result_heap = get_vol(tree, [])

    capacity = 70000000
    free_space = capacity - tree.vol
    need_space = 30000000
    cur_val = 0

    while free_space + cur_val < need_space and len(result_heap):
        cur_val = heappop(result_heap)

    return cur_val


assert (solution_part1('input.test.txt') == 95437)
print('Result Part 1: ', solution_part1('input.txt'))
assert (solution_part2('input.test.txt') == 24933642)
print('Result Part 2: ', solution_part2('input.txt'))
