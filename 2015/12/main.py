from json import load
from collections.abc import Iterable


def is_iterable(obj):
    return isinstance(obj, Iterable)


class Counter(object):
    count: int

    def __init__(self):
        self.count = 0

    def do_count(self, in_data, ignore_red=False):
        if ignore_red and type(in_data) is dict and 'red' in in_data.values():
            return

        if type(in_data) in [list, dict]:
            try:
                for key, item in in_data.items():
                    self.do_count(item, ignore_red)
            except AttributeError:
                for item in in_data:
                    self.do_count(item, ignore_red)

        if type(in_data) is int:
            self.count += in_data


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        file = load(f)

    counter = Counter()
    counter.do_count(file)
    print(f'First result: {counter.count}')
    counter.count = 0
    counter.do_count(file, True)
    print(f'Second result: {counter.count}')
