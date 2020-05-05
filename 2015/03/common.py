directions_map = {
    '^': [0, 1],
    '>': [1, 1],
    'v': [0, -1],
    '<': [1, -1]
}


def move(m, x, step):
    m[x] += step
    return m[0], m[1]

