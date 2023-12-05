import re


def get_symbols(lines: list[str]):
    symbols = {
        symbol
        for line in lines
        for symbol in list(line)
        if not symbol.isdigit() and symbol not in ['\n', '.']
    }
    return symbols


def find_numbers(lines: list[str]):
    pattern = r'\d+'
    result = {}
    for index, line in enumerate(lines):
        matches = re.finditer(pattern, line)

        for match in matches:
            number = int(match.group())
            start = match.start()
            end = match.end() - 1
            result[(index, start, end)] = number

    return result


def get_set_of_adjacents(lines: list[str], cordinates: tuple[int, int, int]):
    # index - 1: start - 1 -> end + 1
    # index :    start - 1 -> end + 1
    # index + 1: start - 1 -> end + 1
    set_of_adjacents = set()
    number_index, start, end = cordinates
    if number_index - 1 >= 0:
        gap = -1
        line = lines[number_index + gap]
        start = start - 1 if start - 1 >= 0 else 0
        end = end + 1 if end + 1 <= len(line) - 1 else len(line) - 1
        for character in line[start:end+1]:
            set_of_adjacents.add(character)

    number_index, start, end = cordinates
    if number_index + 1 <= len(lines) - 1:
        gap = 1
        line = lines[number_index + gap]
        start = start - 1 if start - 1 >= 0 else 0
        end = end + 1 if end + 1 <= len(line) - 1 else len(line) - 1
        for character in line[start:end+1]:
            set_of_adjacents.add(character)

    number_index, start, end = cordinates
    line = lines[number_index]
    start = start - 1 if start - 1 >= 0 else 0
    end = end + 1 if end + 1 <= len(line) - 1 else len(line) - 1
    for character in line[start:end+1]:
        set_of_adjacents.add(character)

    return set_of_adjacents


def sum_parts(lines: list[str]):
    numbers = find_numbers(lines)
    symbols = get_symbols(lines)
    sum = 0
    for cordinates, number in numbers.items():
        adjacents = get_set_of_adjacents(lines, cordinates)
        if adjacents & symbols:
            sum += number
    return sum


with open('./input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# lines = [
#     '467..114..',
#     '...*......',
#     '..35..633.',
#     '......#...',
#     '617*......',
#     '.....+.58.',
#     '..592.....',
#     '......755.',
#     '...$.*....',
#     '.664.598..',
# ]

print(sum_parts(lines))
