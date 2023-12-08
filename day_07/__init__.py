from collections import defaultdict
import bisect

# weakest -> strongest
strengths = ['A', 'K', 'Q', 'J', 'T', '9',
             '8', '7', '6', '5', '4', '3', '2'][::-1]


def convert_card_to_number(cards: str, prefix: str):
    return int(prefix + ''.join([
        str(strengths.index(card) + 10)
        for card in cards
    ]))


def parse_line(line: str):
    return line.split()


def get_number_of_shows(cards: str):
    labels = defaultdict(int)
    for card in cards:
        labels[card] += 1
    return set(labels.values())


def classify_hand(cards: str):
    unique_cards = set(cards)
    number_of_unique_cards = len(unique_cards)
    shows = get_number_of_shows(cards)
    # Five of a kind
    if number_of_unique_cards == 1:
        return 7
    if number_of_unique_cards == 2:
        # Four of a kind
        if shows.issubset({4, 1}):
            return 6
        # Full house
        return 5
    if number_of_unique_cards == 3:
        # Three of a kind
        if shows.issubset({3, 1}):
            return 4
        # Two pair
        return 3
    # One pair
    if number_of_unique_cards == 4:
        return 2
    # High card
    return 1


def get_winnings(lines: list[str]):
    types = [(0, 0)]
    for line in lines:
        hand = parse_line(line)
        classification = classify_hand(hand[0])
        converted_hand = convert_card_to_number(
            hand[0], prefix=str(classification)), int(hand[1])
        bisect.insort(types, converted_hand)
    winnings = 0
    for rank, (_, bid) in enumerate(types[1:], start=1):
        winnings += bid * rank
    return winnings


with open('./input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()


print(get_winnings(lines))
