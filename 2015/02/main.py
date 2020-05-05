# https://adventofcode.com/2015/day/2

def get_surface(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l


def get_extra(dimensions):
    return dimensions[0] * dimensions[1]


def get_bow(l, w, h):
    return l * w * h


def get_ribbon(dimensions):
    return dimensions[0] * 2 + dimensions[1] * 2


if __name__ == '__main__':
    total_paper = 0
    total_ribbon = 0
    with open('./input.txt') as file:
        data = [list(map(int, i.split('x'))) for i in file.read().split()]

    for present_dimensions in data:
        surface = get_surface(*present_dimensions)
        bow = get_bow(*present_dimensions)

        present_dimensions.remove(max(*present_dimensions))

        extra = get_extra(present_dimensions)
        ribbon = get_ribbon(present_dimensions)

        total_paper += surface + extra
        total_ribbon += ribbon + bow

    # part 1
    print(f'Total amount of paper needed: {total_paper}')
    # part 2
    print(f'Total amount of ribbon needed: {total_ribbon}')
