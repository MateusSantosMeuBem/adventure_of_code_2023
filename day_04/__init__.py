def parse_games(line: str):
    victories, guesses = line.split(':')[1].split('|')
    victories = set(victories.split())
    guesses = list(guesses.split())
    return (victories, guesses)


def calculate_game(victories: set[str], guesses: list[str]):
    def is_right_guess(guess):
        return guess in victories

    right_guesses = len(list(filter(is_right_guess, guesses)))
    return 2**(right_guesses - 1) if right_guesses > 0 else 0


def sum_victories(lines: list[str]):
    sum = 0
    for line in lines:
        game = parse_games(line)
        sum += calculate_game(*game)
    return sum


with open('./input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# lines = [
#     'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
#     'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
#     'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
#     'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
#     'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
#     'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
# ]

print(sum_victories(lines))
