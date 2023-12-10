from os.path import dirname, join


def parse_lines(lines: list[str]) -> list[list[int]]:
    return [
        list(map(int, line.split()))
        for line in lines
    ]


def calculate_intervals(line: list[int]):
    return [
        current - line[index - 1]
        for index, current in enumerate(line[1:], start=1)
    ]


def predict_next_number(line: list[int]):
    if not any(line):
        return 0
    return line[-1] + predict_next_number(calculate_intervals(line))


def get_predicted_numbers_sum(lines: list[str]):
    parsed_lines = parse_lines(lines)
    prediction_sum = 0
    for line in parsed_lines:
        predicted = predict_next_number(line[::-1])
        prediction_sum += predicted
    return prediction_sum


FILENAME = 'input.txt'
FILE_PATH = join(dirname(__file__), FILENAME)

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(get_predicted_numbers_sum(lines))
