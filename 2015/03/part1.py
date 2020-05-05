from common import move, directions_map

if __name__ == '__main__':
    current_location = [0, 0]

    with open('./input.txt') as file:
        directions = file.read().replace('\n', '')

    total = {move(current_location, *directions_map[d]) for d in directions}

    # add initial position in case it never gets encountered
    total.add((0, 0))

    print(f"Total homes visited: {len(total)}")
