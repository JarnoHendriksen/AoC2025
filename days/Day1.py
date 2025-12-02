import argparse
import math

import utils


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def parse_line(line):
    dir = line[0]
    num = int(line[1:])
    return dir, num


def run(test_input_path, real_input_path):
    with open(real_input_path, "r") as f:
        real_data = f.read().strip().splitlines()

    with open(test_input_path, "r") as f:
        test_data = f.read().strip().splitlines()

    ##### PART 1 #####
    position = 50
    result1 = 0

    for l in real_data:
        dir, amount = parse_line(l)
        op = add if dir == 'R' else sub
        position = op(position, amount) % 100

        if position == 0:
            result1 += 1

    ##### PART 2 #####
    position = 50
    current_multiple = 0
    result2 = 0

    for l in real_data:
        dir, amount = parse_line(l)
        op = add if dir == 'R' else sub
        op_str = "+" if dir == 'R' else "-"

        utils.log_message("=====")
        utils.log_message(f"Input: {dir}{amount}")
        utils.log_message("old position: " + str(position))

        old_position = position
        position = op(position, amount)

        utils.log_message(f"position{op_str}rotation: {position}")

        if position == 0:
            utils.log_message("Current position is zero")
            result2 += 1
            continue

        if dir == 'L' and amount == old_position:
            utils.log_message(
                "Left rotation equal to position, setting position to 0")
            position = 0
            result2 += 1
            continue

        if dir == 'R' and (100 - amount) == old_position:
            utils.log_message(
                "Right rotation equal to position, setting position to 0")
            position = 0
            result2 += 1
            continue

        if dir == 'L' and amount > old_position and old_position != 0 and (amount/100) >= 1:
            while position < 0:
                position += 100
                utils.log_message(f"position underflow, new pos: {position}")
                result2 += 1
            continue

        if dir == 'R' and amount + old_position > 100 and old_position != 0 and (amount/100) >= 1:
            while position >= 100:
                position -= 100
                utils.log_message(f"position overflow, new pos: {position}")
                result2 += 1

        if position < 0:
            position = position % 100

    return (result1, result2)


if __name__ == "__main__":
    utils.verbosity = 3
    part1_result, part2_result = run(
        "../inputs/day1test.txt", "../inputs/day1real.txt")
    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")
