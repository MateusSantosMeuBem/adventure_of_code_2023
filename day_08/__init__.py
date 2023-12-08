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
    for line in lines[2:]:
        key, coordinate = parse_line(line)
        coordinates[key] = coordinate

    steps = 0
    foot = 'AAA'
    last_point = 'ZZZ'
    while foot != last_point:
        for direction in directions:
            steps += 1
            index = DIRECTIONS_INDEX[direction]
            foot = coordinates[foot][index]
    return steps


with open(r'./input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(get_steps_number(lines))
