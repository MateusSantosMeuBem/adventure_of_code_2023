from os.path import dirname, join
from pprint import pprint


def is_empty_space(space: str):
    return space.count('.') == len(space)


def get_empty_lines(lines: list[str]):
    empty_lines = []
    for index, line in enumerate(lines):
        if is_empty_space(line):
            empty_lines.append(index)
    return sorted(empty_lines)


def get_empty_columns(lines: list[str]):
    empty_columns = []
    first_line = lines[0]
    for column_index in range(len(first_line)):
        column = [line[column_index] for line in lines]
        if is_empty_space(column):
            empty_columns.append(column_index)
    return sorted(empty_columns)


def expand_lines(lines: list[str], empty_lines: list[int]):
    empty_space = '.' * len(lines[0])
    for empty_line in empty_lines[::-1]:
        lines.insert(empty_line, empty_space)


def expand_columns(lines: list[str], empty_columns: list[int]):
    for line_index, _ in enumerate(lines):
        for empty_column in empty_columns[::-1]:
            converted_line = list(lines[line_index])
            converted_line.insert(empty_column, '.')
            lines[line_index] = ''.join(converted_line)


def get_galaxies(lines: list[str]):
    galaxies = set()
    for line, _ in enumerate(lines):
        for column, value in enumerate(lines[line]):
            if value == '#':
                galaxies.add((line, column))
    return galaxies


def get_pair_galaxies(galaxies: set[tuple[int]]):
    pairs = set()
    for galay_a in galaxies:
        for galay_b in galaxies:
            pair = (galay_a, galay_b)
            inverted_pair = (galay_b, galay_a)
            if pair not in pairs and inverted_pair not in pairs and galay_a != galay_b:
                pairs.add((galay_a, galay_b))
    return pairs


def calculate_distance(x1, y1, x2, y2):
    return abs(y1 - y2) + abs(x1 - x2)


def calculate_pair_distances(pairs: set[tuple[int]]):
    my_sum = 0
    for pair in pairs:
        galaxy_a, galaxy_b = pair
        my_sum += calculate_distance(*galaxy_a, *galaxy_b)
    return my_sum


def expand_universe(lines: list[str]):
    empty_lines = get_empty_lines(lines)
    empty_columns = get_empty_columns(lines)
    expand_lines(lines, empty_lines)
    expand_columns(lines, empty_columns)
    galaxies = get_galaxies(lines)
    pairs = get_pair_galaxies(galaxies)
    pair_distances = calculate_pair_distances(pairs)
    print(pair_distances)


FILENAME = 'input.txt'
FILE_PATH = join(dirname(__file__), FILENAME)

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    lines = file.read().split('\n')

print(expand_universe(lines))
