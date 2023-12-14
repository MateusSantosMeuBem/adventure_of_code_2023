from os.path import dirname, join
from pprint import pprint


def get_horizontal_reflection(field: list[str]):
    all_mirrors = 0
    for index, line in enumerate(field[1:], start=1):
        previous_line = field[index-1]
        if previous_line == line:
            up_part = field[:index]
            bottom_part = field[index:]
            shortest_part = min(len(up_part), len(bottom_part))
            up_part = up_part[-shortest_part:]
            bottom_part = bottom_part[:shortest_part]
            if up_part == bottom_part[::-1]:
                if index > all_mirrors:
                    all_mirrors += index * 100
    return all_mirrors


def get_vertical_reflection(field: list[str]):
    all_mirrors = 0
    for index in range(1, len(field[0])):
        previous_column = [line[index-1] for line in field]
        column = [line[index] for line in field]
        if previous_column == column:
            shortest_part = min(index-1, len(field[0])-index)
            left_part = [
                line[index-shortest_part:index]
                for line in field
            ]
            right_part = [
                line[index:index+shortest_part][::-1]
                for line in field
            ]
            if left_part == right_part:
                if index > all_mirrors:
                    all_mirrors = index
    return all_mirrors


def get_result(fields: list[str]):
    sum_reflections = 0
    for field in fields:
        field = field.split('\n')
        horizontal, vertical = get_horizontal_reflection(
            field), get_vertical_reflection(field)
        sum_reflections += horizontal + vertical
    return sum_reflections


FILENAME = 'input.txt'
FILE_PATH = join(dirname(__file__), FILENAME)

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    lines = file.read().split('\n\n')

print(get_result(lines))
