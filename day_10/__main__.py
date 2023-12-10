from os.path import dirname, join

pipes_translator = {
    '|': {'|': [(0, -1), (0, 1)], 'L': [(0, 1)], 'J': [(0, 1)], 'F': [(0, -1)], '7': [(0, -1)], '-': []},

    '-': {'-': [(-1, 0), (1, 0)], 'L': [(-1, 0)], 'J': [(1, 0)], 'F': [(-1, 0)], '7': [(1, 0)], '|': []},

    'L': {'-': [(1, 0)], '|': [(0, -1)], 'J': [(1, 0)], 'F': [(0, -1)], '7': [(0, -1), (1, 0)], 'L': []},

    'J': {'-': [(-1, 0)], '|': [(0, -1)], 'L': [(-1, 0)], 'F': [(-1, 0), (0, -1)], '7': [(0, -1)], 'J': []},

    'F': {'-': [(1, 0)], '|': [(0, 1)], 'L': [(0, 1)], 'J': [(1, 0), (0, 1)], '7': [(1, 0)], 'F': []},

    '7': {'-': [(-1, 0)], '|': [(0, 1)], 'L': [(0, 1), (-1, 0)], 'F': [(-1, 0)], 'J': [((0, 1))], '7': []},
}

not_pipes = [
    '.'
]


def convert_xy_to_line_and_column(coordinates: tuple[int]):
    return coordinates[::-1]


def get_s_position(lines: list[str]):
    """
    Return line and column,instead of x and y.
    """
    for x, line in enumerate(lines):
        for y, value in enumerate(line):
            if value == 'S':
                return (x, y)  # (line, column)


def get_neighbors(lines: list[str], initial_position: tuple[int]):
    neighboors = []
    shifts = [0, 0, -1, 1]
    x, y = initial_position
    for x_shit, y_shit in zip(shifts, shifts[::-1]):
        try:
            line, column = x + x_shit, y + y_shit
            neighboor = lines[line][column]
            if neighboor and line >= 0 and column >= 0 and neighboor not in not_pipes:
                neighboors.append((line, column))
        except:
            continue
    return neighboors


def is_valid_change(lines: list[str], pipe: tuple[int], neighbor: tuple[int], pipe_label: str = None):
    pipe_label = pipe_label if pipe_label else lines[pipe[0]][pipe[1]]
    neighbor_label = lines[neighbor[0]][neighbor[1]]
    if neighbor_label != 'S':
        valid_moves = list(map(convert_xy_to_line_and_column,
                               pipes_translator[pipe_label][neighbor_label]))
        pipe_neighbor_diff = (neighbor[0] - pipe[0], neighbor[1] - pipe[1])
        for valid_move in valid_moves:
            if pipe_neighbor_diff == valid_move:
                return True
    return False


def get_initial_pipe_label(lines: list[str], s: tuple[int], neighbors: list[tuple[int]]):
    pipes = {}
    for pipe_label in pipes_translator:
        pipes[pipe_label] = []
        for neighbor in neighbors:
            if is_valid_change(lines, s, neighbor, pipe_label):
                pipes[pipe_label].append(neighbor)
                if len(pipes[pipe_label]) == 2:
                    return pipe_label


def get_next_pipe(pipe: tuple[int], neighbors: list[tuple[int]], visited: set[tuple[int]], pipe_label: str = None):
    next_pipes = set()
    for neighbor in neighbors:
        if is_valid_change(lines, pipe, neighbor, pipe_label) and neighbor not in visited:
            next_pipes.add(neighbor)
    diff = list(next_pipes - visited.intersection(next_pipes))
    return diff[0]


def replace_s(lines: list[str], s_position: tuple[int], new_label: str):
    line = list(lines[s_position[0]])
    line[s_position[1]] = new_label
    lines[s_position[0]] = ''.join(line)


def get_longest_path(lines: list[str]):
    s_position = get_s_position(lines)
    first_neighbors = get_neighbors(lines, s_position)
    initial_pipe_label = get_initial_pipe_label(
        lines, s_position, first_neighbors)
    replace_s(lines, s_position, initial_pipe_label)
    next_neighbor = get_next_pipe(s_position,
                                  first_neighbors, set(), initial_pipe_label)
    step_counter = 0
    visited_pipes = {s_position}
    while next_neighbor != s_position:
        visited_pipes.add(next_neighbor)
        step_counter += 1
        label = lines[next_neighbor[0]][next_neighbor[1]]
        neighbors = get_neighbors(lines, next_neighbor)
        try:
            next_neighbor = get_next_pipe(next_neighbor,
                                          neighbors, visited_pipes, label)
        except:
            next_neighbor = s_position
            step_counter += 1
    return step_counter


FILENAME = 'input.txt'
FILE_PATH = join(dirname(__file__), FILENAME)

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    lines = file.read().split('\n')

print(get_longest_path(lines))
