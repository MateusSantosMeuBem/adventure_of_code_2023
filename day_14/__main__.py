from os.path import dirname, join
from pprint import pprint


def parse_platform(platfmor: list[str]):
    return [
        list(line)
        for line in platfmor
    ]


def tilt_platform(platfmor: list[str]):
    for index, line in enumerate(platfmor[1:], start=1):
        for space_index, (space, previous_space) in enumerate(zip(line, platfmor[index-1])):
            if space == 'O' and previous_space == '.':
                platfmor[index][space_index], platfmor[index -
                                                       1][space_index] = previous_space, space


def calculate_weights(platform: list[str]):
    weights_sum = 0
    platform_length = len(platform)
    for line_index, line in enumerate(platform):
        for _, space in enumerate(line):
            if space == 'O':
                weights_sum += platform_length - line_index
    return weights_sum


def get_weights(platform: list[str]):
    platform = parse_platform(platform)
    for _ in range(len(platform)):
        tilt_platform(platform)
    return calculate_weights(platform)


FILENAME = 'input.txt'
FILE_PATH = join(dirname(__file__), FILENAME)

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    platform = file.read().split('\n')

print(get_weights(platform))
