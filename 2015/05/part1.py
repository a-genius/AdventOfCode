def is_valid(word):
    vowels_count = 0
    repeats = False
    for bad in ['ab', 'cd', 'pq', 'xy']:
        if bad in word:
            return False

    for i, letter in enumerate(word):
        if letter in 'aeiou':
            vowels_count += 1

        if letter == word[i - 1] and i > 0:
            repeats = True

    if repeats and vowels_count >= 3:
        return True

    return False


if __name__ == '__main__':
    with open('./input.txt') as file:
        words = file.read().split()

    nice = [w for w in words if is_valid(w)]

    print(f'Total nice words: {len(nice)}')
