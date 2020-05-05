import string

in_pass = "vzbxkghb"
banned = ['i', 'o', 'l']
chars = [ch for ch in list(string.ascii_lowercase) if ch not in banned]


def check_doubles(password):
    pairs = [f'{"".join((a, b))}' for a, b in zip(password, password[1:]) if a == b]
    if len(pairs) >= 2 and pairs[0] != pairs[1] and (password.index(pairs[1]) - password.index(pairs[0])) >= 3:
        return True
    return False


def check_seq(password):
    a = [True for a, b, c in zip(password, password[1:], password[2:])
         if chars.index(c) - chars.index(b) == 1 and chars.index(b) - chars.index(a) == 1]

    return a


def rotate(password, i=-1):
    password = list(password)
    inx = chars.index(password[i])
    if inx < len(chars) - 1:
        password[i] = chars[inx + 1]
    else:
        password[i] = chars[0]
        i -= 1
        return rotate(password, i)

    return ''.join(password)


def get_next(password):
    password = rotate(password)
    while not (check_seq(password) and check_doubles(password)):
        password = rotate(password)

    return password


if __name__ == '__main__':
    new_pass = get_next(in_pass)
    print(f'First pass: {new_pass}')
    print(f'Second pass: {get_next(new_pass)}')
