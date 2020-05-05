import numpy as np
from pprint import pprint
import sys

np.set_printoptions(threshold=sys.maxsize)


def parse_line(line):
    parts = line.split()
    x1, y1 = parts[1].split(',') if parts[0] == 'toggle' else parts[2].split(',')
    x2, y2 = parts.pop().split(',')
    instruction = parts[0] if parts[0] == 'toggle' else parts[1]

    return instruction, int(x1), int(y1), int(x2) + 1, int(y2) + 1


def part_one(input):
    grid = np.zeros((1000, 1000))
    m = {
        'on': 1,
        'off': 0,
    }

    for line in input:
        if not line:
            continue
        instruction, x1, y1, x2, y2 = parse_line(line)
        grid[x1:x2, y1:y2] = m[instruction] if instruction != 'toggle' \
            else (grid[x1:x2, y1:y2] - np.ones((abs(x1 - x2), abs(y1 - y2)))) * -1

    print(f'total lights in part one {grid.sum()}')


def part_two(input):
    grid = np.zeros((1000, 1000))
    m = {
        'on': 1,
        'toggle': 2,
        'off': -1
    }

    for line in input:
        if not line:
            continue
        instruction, x1, y1, x2, y2 = parse_line(line)
        grid[x1:x2, y1:y2] = grid[x1:x2, y1:y2] + m[instruction]

        # as brightness can not be lower than 0, we will eliminate all negatives
        negative = np.where(grid < 0)
        if len(negative[0]):
            for x, y in zip(negative[0], negative[1]):
                grid[x][y] = 0

    print(f'total lights in part two {grid.sum()}')


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        file = f.read().split('\n')
        part_one(file)
        part_two(file)

