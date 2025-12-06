import math

import utils


def argmax(array):
    return array.index(max(array))


def shift_if_larger(new_dig: str, current_sequence: list[str]) -> str:
    utils.log_message(current_sequence)

    new_seq_repl = [current_sequence[0], new_dig]
    new_seq_shift = [current_sequence[1], new_dig]

    candidates = [current_sequence, new_seq_repl, new_seq_shift]

    max_idx = argmax(list(map(lambda x: int("".join(x)), candidates)))

    utils.log_message(candidates)
    utils.log_message(candidates[max_idx])

    return candidates[max_idx]


def digs_to_str(*digs):
    result = 0

    for i in reversed(range(len(digs))):
        result += int(digs[i]) * math.pow(10, 11-i)

    return result


def run(test_input_path, real_input_path):
    with open(test_input_path, "r") as f:
        test_data = f.read().strip().splitlines()

    with open(real_input_path, "r") as f:
        real_data = f.read().strip().splitlines()

    data = real_data

    ##### PART 1 #####

    result1 = 0

    for l in data:
        max_digs = ['0', '0']

        utils.log_message(max_digs)

        for i in range(len(l)):
            max_digs = shift_if_larger(l[i], max_digs)

        result1 += int("".join(max_digs))

    ##### PART 2 #####
    result2 = 0
    line_len = len(data[0])
    for line in data:
        max_val = 0
        for i1 in range(0, line_len):
            for i2 in range(i1, line_len):
                for i3 in range(i2, line_len):
                    for i4 in range(i3, line_len):
                        for i5 in range(i4, line_len):
                            for i6 in range(i5, line_len):
                                for i7 in range(i6, line_len):
                                    for i8 in range(i7, line_len):
                                        for i9 in range(i8, line_len):
                                            for i10 in range(i9, line_len):
                                                for i11 in range(i10, line_len):
                                                    for i12 in range(i11, line_len):
                                                        num = digs_to_str(
                                                            line[i1], line[i2], line[i3], line[i4], line[i5], line[i6], line[i7], line[i8], line[i9], line[i10], line[i11], line[i12])
                                                        max_val = max(
                                                            max_val, num)

        result2 += max_val

    return (result1, result2)


if __name__ == "__main__":
    utils.verbosity = 0
    part1_result, part2_result = run(
        "../inputs/day3test.txt", "../inputs/day3real.txt")
    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")
