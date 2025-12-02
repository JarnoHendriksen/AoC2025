
def run(input_part1_path, input_part2_path):
    with open(input_part1_path, "r") as f:
        data_part1 = f.read().strip().splitlines()

    with open(input_part2_path, "r") as f:
        data_part2 = f.read().strip().splitlines()

    # TODO: Implement solutions

    return (0, 0)


if __name__ == "__main__":
    part1_result, part2_result = run(
        "../inputs/day1test.txt", "../inputs/day1real.txt")
    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")
