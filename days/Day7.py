

def check_collisions(line: str, positions: list[int]) -> tuple[list[int], int]:
    new_positions = []
    collisions = 0

    for p in positions:
        if line[p] == '^':
            new_positions.append(p-1)
            new_positions.append(p+1)
            collisions += 1
        else:
            new_positions.append(p)

    return new_positions, collisions


def unique(l: list[int]):
    return [*{*l}]


def run(test_input_path, real_input_path):
    with open(test_input_path, "r") as f:
        test_data = f.read().splitlines()

    with open(real_input_path, "r") as f:
        real_data = f.read().splitlines()

    data = real_data

    positions = []

    result1 = 0

    # Find starting point
    start_pos = data[0].index('S')
    positions.append(start_pos)

    for l in data:
        new_positions, collision_count = check_collisions(l, positions)
        positions = unique(new_positions)
        result1 += collision_count

    return (result1, 0)


if __name__ == "__main__":
    part1_result, part2_result = run(
        "../inputs/day7test.txt", "../inputs/day7real.txt")
    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")
