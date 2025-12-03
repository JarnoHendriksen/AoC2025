
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


def run(test_input_path, real_input_path):
    with open(test_input_path, "r") as f:
        test_data = f.read().strip().splitlines()

    with open(real_input_path, "r") as f:
        real_data = f.read().strip().splitlines()

    data = real_data

    result1 = 0

    for l in data:
        max_digs = ['0', '0']

        utils.log_message(max_digs)

        for i in range(len(l)):
            max_digs = shift_if_larger(l[i], max_digs)

        result1 += int("".join(max_digs))

    return (result1, 0)


if __name__ == "__main__":
    utils.verbosity = 0
    part1_result, part2_result = run(
        "../inputs/day3test.txt", "../inputs/day3real.txt")
    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")
