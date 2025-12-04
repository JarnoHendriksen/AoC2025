
def count_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            if grid[ny][nx] == "@":
                count += 1
    return count


def run(test_input_path, real_input_path):
    with open(test_input_path, "r") as f:
        test_data = f.read().strip().splitlines()

    with open(real_input_path, "r") as f:
        real_data = f.read().strip().splitlines()

    data = real_data

    result1 = 0

    print(f"Grid dimensions: {len(data)}, {len(data[0])}")

    ##### PART 1 #####
    for y in range(len(data)):
        for x in range(len(data[y])):
            neighbors = count_neighbors(data, x, y)
            if neighbors < 4 and data[y][x] == '@':
                result1 += 1

    ##### PART 2 #####
    result2 = 0
    while True:
        removable_papers = 0
        for y in range(len(data)):
            for x in range(len(data[y])):
                neighbors = count_neighbors(data, x, y)
                if neighbors < 4 and data[y][x] == '@':
                    removable_papers += 1
                    temp_line = list(data[y])
                    temp_line[x] = '.'
                    data[y] = "".join(temp_line)
                    result2 += 1

        if removable_papers == 0:
            break

    return (result1, result2)


if __name__ == "__main__":
    part1_result, part2_result = run(
        "../inputs/day4test.txt", "../inputs/day4real.txt")
    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")
