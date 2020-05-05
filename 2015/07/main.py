from copy import copy


def get_part(input):
    try:
        part = str(int(input))
    except:
        part = f'buffer["{input}"]'

    return part


def evaluate_buffer(buffer):
    while type(buffer['a']) is not int:
        for key, value in buffer.items():
            try:
                buffer[key] = eval(value)
            except (NameError, TypeError, KeyError):
                pass


def populate_buffer(lines):
    buffer = {'a': None}

    for line in lines:
        parts = line.split()
        if 'NOT' in line:
            buffer[parts.pop()] = '~' + f'buffer["{parts[1]}"]'
            continue
        elif parts[1] in list(operation.keys())[:-1]:
            part_1 = get_part(parts[0])
            part_2 = get_part(parts[2])
            buffer[parts.pop()] = ' '.join([part_1, f'{operation[parts[1]]}', part_2])
            continue
        else:
            part = get_part(parts[0])
            buffer[parts.pop()] = part
            continue

    return buffer, copy(buffer)


if __name__ == '__main__':
    operation = {
        'AND': '&',
        'RSHIFT': '>>',
        'LSHIFT': '<<',
        'OR': '|',
        'NOT': '65535 -'
    }

    with open('./input.txt', 'r') as f:
        lines = f.read().split('\n')[:-1]
        lines.sort()

    buffer, buffer_copy = populate_buffer(lines)
    evaluate_buffer(buffer)
    buffer_copy['b'] = buffer['a']
    for key, value in buffer_copy.items():
        if type(value) is str:
            buffer_copy[key] = value.replace('buffer', 'buffer_copy')

    evaluate_buffer(buffer_copy)
    print('Answer: ', buffer['a'])
    print('Answer part two: ', buffer_copy['a'])
