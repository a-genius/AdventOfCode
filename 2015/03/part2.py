from common import move, directions_map

if __name__ == '__main__':
    current_location_santa = [0, 0]
    current_location_robot = [0, 0]

    with open('./input.txt') as file:
        directions = file.read().replace('\n', '')

    total = [move(current_location_santa, *directions_map[d]) for i, d in enumerate(directions) if i % 2 == 0]
    total2 = [move(current_location_robot, *directions_map[d]) for i, d in enumerate(directions) if i % 2 != 0]

    # add initial position to the lists in case these never get encountered during the trip
    total.append((0, 0))
    total2.append((0, 0))

    print(f'Total homes visited: {len({*total, *total2})}')

