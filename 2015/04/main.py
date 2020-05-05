import hashlib

if __name__ == '__main__':
    coin = 0
    # switch to not print hashes with 5 leading zeros if it was found already
    looking_for_five = True

    while True:
        test_hash = hashlib.md5(('yzbqklnj' + str(coin)).encode()).hexdigest()
        if test_hash.startswith('00000') and looking_for_five:
            looking_for_five = False
            print(f'00000 -> {coin}')

        if test_hash.startswith('000000'):
            print(f'000000 -> {coin}')
            break

        coin += 1


