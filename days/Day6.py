from collections.abc import Callable


class Parser:
    def __init__(self, input):
        self.input = input
        self.position = 0

    def peek(self) -> str:
        if self.position < len(self.input):
            return self.input[self.position]
        else:
            return None

    def consume(self) -> str:
        if self.position < len(self.input):
            self.position += 1
            return self.input[self.position - 1]
        else:
            return None


def parse_symbol(char: str | None, fn: Callable[[str], bool]):
    if char == None:
        return False
    else:
        return fn(char)\



def parse_line(line: str) -> list[int | str]:
    result = []
    parser = Parser(line)

    while parser.peek() != None:
        consumed_chars = []
        is_number = False

        while parse_symbol(parser.peek(), lambda x: x == ' '):
            parser.consume()  # consume spaces, but don't store them

        while parse_symbol(parser.peek(), lambda x: x.isdigit()):
            consumed_chars.append(parser.consume())
            is_number = True

        while parse_symbol(parser.peek(), lambda x: x == '+' or x == '*'):
            consumed_chars.append(parser.consume())

        if len(consumed_chars) > 0:
            if is_number:
                result.append(int("".join(consumed_chars)))
            else:
                # operators should only be one char
                result.append(consumed_chars[0])

    return result


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def run(test_input_path, real_input_path):
    with open(test_input_path, "r") as f:
        test_data = f.read().splitlines()

    with open(real_input_path, "r") as f:
        real_data = f.read().splitlines()

    data = real_data

    parsed_data = []

    for line in data:
        parsed_line = parse_line(line)
        parsed_data.append(parsed_line)

    # Transpose data so each operation is in its own list
    operations = list(map(list, zip(*parsed_data)))

    result1 = 0
    i = 1
    for op in operations:
        print(f"Evaluating operation {i}/{len(operations)}")
        i += 1
        operator = add if op[-1] == '+' else mult
        op = op[:-1]  # remove operator from list

        acc = 0 if operator == add else 1
        [acc := operator(acc, x) for x in op]

        result1 += acc

    return (result1, 0)


if __name__ == "__main__":
    part1_result, part2_result = run(
        "../inputs/day6test.txt", "../inputs/day6real.txt")
    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")
