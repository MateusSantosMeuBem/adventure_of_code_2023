meta_game = {
    'red': 12, 'green': 13, 'blue': 14,
}


def format_subgame(subgame):
    return {
        cubes.split()[1]: int(cubes.split()[0])
        for cubes in subgame.split(',')
    }


def valid_game_sum(lines: list[str]):
    sum = 0
    for id, line in enumerate(lines, start=1):
        line = line.split(':')[1]
        game = [
            format_subgame(subgame)
            for subgame in line.split(';')
        ]
        is_valid_game = all([
            True if subgame.get('red', 0) <= meta_game.get('red', 0) and subgame.get('green', 0) <= meta_game.get(
                'green', 0) and subgame.get('blue', 0) <= meta_game.get('blue', 0) else False
            for subgame in game
        ])
        if is_valid_game:
            sum += id

    return sum


with open('./input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# lines = [
#     'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
#     'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
#     'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
#     'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
#     'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
# ]

print(valid_game_sum(lines))
