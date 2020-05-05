import re

pair_re = re.compile(r"(..).*\1")
repeat_re = re.compile(r"(.).\1")


def is_nice2(word):
    if repeat_re.search(word) is None:
        return False
    return pair_re.search(word) is not None


if __name__ == '__main__':
    with open('./input.txt') as file:
        words = file.read().split()

        nice = [w for w in words if is_nice2(w)]

        print(f'Total nice words: {len(nice)}')
