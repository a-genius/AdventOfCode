def look_and_say(data, max, counter=0):
    ret = last_char = ''
    count = 0
    counter += 1
    for ind, char in enumerate(data):
        if ind == 0:
            last_char = char
            count += 1
            continue

        if char == last_char:
            count += 1
        else:
            ret += str(count) + last_char
            count = 1
            last_char = char

        if ind == len(data) - 1:
            ret += str(count) + last_char

    if counter == 40:
        print(f'Part one result: {len(ret)}')

    if counter == max:
        return ret

    return look_and_say(ret, max, counter)


print(f'Part two result: {len(look_and_say("1113222113", 50))}')
