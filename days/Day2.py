import math

import utils


def check_pattern_twice(number, pattern: str) -> bool:
    pat_len = len(pattern)
    pat_int = int(pattern)

    temp_num = (number - pat_int) / math.pow(10, pat_len)

    if pat_int == temp_num:
        return True
    else:
        return False


def check_pattern_multiple(number, pattern: str) -> bool:
    temp_num = number
    pat_len = len(pattern)
    pat_int = int(pattern)

    while True:
        temp_num = (temp_num - pat_int) / math.pow(10, pat_len)

        if temp_num == 0:
            return True
        elif int(temp_num) == temp_num and temp_num >= pat_int:
            continue
        else:
            return False


def has_pattern_twice(number: int) -> bool:
    number_str = str(number)
    digit_count = len(number_str)

    for i in reversed(range(digit_count)):
        if (i < digit_count / 2):
            break

        tail = number_str[i:]
        if tail[0] == '0':  # number can't start with 0
            continue

        has_pattern = check_pattern_twice(number, tail)
        if has_pattern:
            return True

    return False


def has_pattern_multiple(number: int) -> bool:
    number_str = str(number)
    digit_count = len(number_str)

    for i in reversed(range(digit_count)):
        if (i < digit_count / 2):
            break

        tail = number_str[i:]
        if tail[0] == '0':  # number can't start with 0
            continue

        has_pattern = check_pattern_multiple(number, tail)
        if has_pattern:
            return True

    return False


def run(test_input_path, real_input_path):
    with open(real_input_path, "r") as f:
        real_data = f.read().strip().split(',')

    with open(test_input_path, "r") as f:
        test_data = f.read().strip().split(',')

    data = real_data

    result1 = 0
    result2 = 0
    for r in data:
        range_ = r.split('-')
        min_val = int(range_[0])
        max_val = int(range_[1])

        for i in range(min_val, max_val+1):
            if has_pattern_twice(i):
                result1 += i
            if has_pattern_multiple(i):
                result2 += i

    return (result1, result2)


if __name__ == "__main__":
    utils.verbosity = 3
    part1_result, part2_result = run(
        "../inputs/day1test.txt", "../inputs/day1real.txt")
    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")
