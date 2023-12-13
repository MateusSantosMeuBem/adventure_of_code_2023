from os.path import dirname, join


def parse_line(line: str) -> list[tuple[str, tuple[int]]]:
    mask, groups = line.split()
    return mask, tuple(map(int, groups.split(',')))


def get_possibilities(mask: str, groups: tuple[int]):
    literal_groups = [
        '#' * group
        for group in groups
    ]
    n_okay_springs = len(mask) - sum(groups)
    first_possibility = ''
    for index in range(max(n_okay_springs, len(literal_groups))):
        try:
            first_possibility += literal_groups[index]
            if n_okay_springs > index:
                first_possibility += '.'
        except:
            if n_okay_springs > index:
                first_possibility += '.'
    print(first_possibility)


def get_number_of_all_possibilities(lines: list[str]):
    for line in lines:
        mask, groups = parse_line(line)
        possibilities = get_possibilities(mask, groups)


FILENAME = 'input_test.txt'
FILE_PATH = join(dirname(__file__), FILENAME)

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    lines = file.read().split('\n')

print(get_number_of_all_possibilities(lines))
