DIRECTIONS_INDEX = {
    'L': 0,
    'R': 1,
}


def parse_line(line: str) -> tuple[str, list[str, str]]:
    key, coordinates = line.split(' = ')
    coordinates = coordinates.replace('\n', '')[1:-1].split(', ')
    return (key, coordinates)


def get_steps_number(lines: list[str]) -> int:
    directions = lines[0].replace('\n', '')
    coordinates = {}
    ends_with_A = set()
    for line in lines[2:]:
        key, coordinate = parse_line(line)
        coordinates[key] = coordinate
        if key.endswith('A'):
            ends_with_A.add(key)

    steps = 0
    last_point = 'ZZZ'
    short_path = len(coordinates) * 2
    longest_path = 0
    for ends in ends_with_A:
        foot = ends
        while not foot.endswith('Z'):
            for direction in directions:
                steps += 1
                index = DIRECTIONS_INDEX[direction]
                foot = coordinates[foot][index]
        short_path = steps if steps <= short_path else 0
        longest_path = steps if steps >= longest_path else 0
    return (short_path, longest_path)


with open(r'.\input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(get_steps_number(lines))
