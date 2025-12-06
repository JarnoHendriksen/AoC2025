

def merge_if_overlap(r1: tuple[int, int], r2: tuple[int, int]):
    if is_overlapping_or_touching(r1, r2):
        return (min(r1[0], r2[0]), max(r1[1], r2[1]))
    else:
        return None


def merge_range_list(ranges: list[tuple[int, int]]) -> tuple[int, int]:
    min_vals = [x[0] for x in ranges]
    max_vals = [x[1] for x in ranges]

    return (min(min_vals), max(max_vals))


def is_overlapping_or_touching(r1: tuple[int, int], r2: tuple[int, int]) -> bool:
    return (r1[0] < r2[0] < r1[1] or r2[0] < r1[0] < r2[1] or r1[1]+1 == r2[0] or r2[1]+1 == r1[0])


def count_gaps(ranges: list[tuple[int, int]]) -> int:
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    total_gap_size = 0

    for i in range(len(sorted_ranges) - 1):
        gap_size = sorted_ranges[i+1][0] - sorted_ranges[i][1]

        if gap_size > 0:
            total_gap_size += gap_size

    max_val = max([r[1] for r in sorted_ranges])
    total_size = max_val - sorted_ranges[0][0] + 2

    return total_size - total_gap_size


def parse_range(r: str) -> tuple[int, int]:
    split_str = r.split('-')

    return (int(split_str[0]), int(split_str[1]))


def parse_ranges(ranges: list[str]) -> list[tuple[int, int]]:
    parsed_ranges = []

    j = 0

    for r in ranges:
        parsed_range = parse_range(r)
        parsed_ranges.append(parsed_range)

        j += 1

    return parsed_ranges


def is_in_range(r: tuple[int, int], number: int) -> bool:
    return r[0] <= number <= r[1]


def run(test_input_path, real_input_path):
    with open(test_input_path, "r") as f:
        test_data = f.read().splitlines()

    with open(real_input_path, "r") as f:
        real_data = f.read().splitlines()

    data = real_data

    ##### PART 1 #####
    result1 = 0
    ranges = []
    idx = 0
    while data[idx] != '':
        ranges.append(data[idx])
        idx += 1

    idx += 1  # skip empty line
    ranges = parse_ranges(ranges)

    while idx < len(data):
        ingredient_id = int(data[idx])

        for r in ranges:
            if is_in_range(r, ingredient_id):
                result1 += 1
                break

        idx += 1

    ##### PART 2 #####
    result2 = count_gaps(ranges)

    return (result1, result2)


if __name__ == "__main__":
    part1_result, part2_result = run(
        "../inputs/day5test.txt", "../inputs/day5real.txt")
    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")
