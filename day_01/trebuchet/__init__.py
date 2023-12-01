DECIMALS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_sum_of_digits(
        lines: list[str],
        use_spelled_digits: bool = False,
):
    """Sum of join of first and last digit of each line.
    If `use_spelled_digits` True use check for it for
    spelled digits (e.g. 'one', 'five') either.

    Args:
        lines (list[str]): Lines to iterate over.
        use_spelled_digits (bool): Use spelled digits or not.

    Return (bool): Sum of join of first and last digit of each line. 
    """
    sum = 0
    for line in lines:
        line = line.replace('\n', '')
        left, right = 0, len(line) - 1
        while not (line[left].isdigit() and line[right].isdigit()) and left <= right:
            left = left + 1 if not line[left].isdigit() else left
            right = right - 1 if not line[right].isdigit() else right
        left_number, right_number = line[left], line[right]

        if use_spelled_digits:
            found_from_left = {
                line.find(decimal): DECIMALS.get(decimal)
                for decimal in DECIMALS
                if line.find(decimal) != -1
            }
            found_from_right = {
                line.rfind(decimal): DECIMALS.get(decimal)
                for decimal in DECIMALS
                if line.find(decimal) != -1
            }
            spell_found = {
                **found_from_left, **found_from_right
            }

            sorted_keys = sorted(spell_found)

            if len(sorted_keys) == 1:
                spell_unique = spell_found.get(sorted_keys[0])
                left_number = spell_unique if sorted_keys[0] < left else left_number
                right_number = spell_unique if sorted_keys[0] > right else right_number
            elif len(sorted_keys) > 1:
                spell_left, spell_right = spell_found.get(
                    sorted_keys[0]), spell_found.get(sorted_keys[-1])
                left_number = spell_left if sorted_keys[0] < left else left_number
                right_number = spell_right if sorted_keys[-1] > right else right_number

        sum += int(left_number + right_number)
    return sum


with open('./input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(get_sum_of_digits(lines))
