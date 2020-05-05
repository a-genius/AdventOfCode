def part_one(lines):
    literals = in_memory = encoded = 0

    for line in lines:
        literals += len(line)
        in_memory += len(bytes(line[1:-1], encoding='utf-8').decode('unicode_escape'))
        encoded += len('"{}"'.format(line.replace('\\', '\\\\').replace('"', '\\"')))

    return literals, in_memory, encoded


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        file = f.read().split('\n')[:-1]

    literal, actual, new_literal = part_one(file)
    print(f"Part one result: {literal - actual}")
    print(f"Part two result: {new_literal - literal}")
