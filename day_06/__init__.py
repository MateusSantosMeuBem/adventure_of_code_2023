def parse_data(lines: list[str], join_line_values=False) -> int:
    times = map(int, lines[0].split(':')[-1].split())
    distances = map(int, lines[1].split(':')[-1].split())
    if join_line_values:
        times = int(''.join(map(str, times)))
        distances = int(''.join(map(str, distances)))
    return [(times, distances)] if join_line_values else zip(times, distances)


def get_ways_to_win(time: int, distance_record: int) -> int:
    ways_to_win = 0
    for second_holding_button in range(0, time + 1):
        time_to_run = time - second_holding_button
        distance = second_holding_button * time_to_run
        ways_to_win += 1 if distance > distance_record else 0
    return ways_to_win


def get_product_of_winning_ways(lines: list[str]):
    margin = 1
    parsed_data = parse_data(lines, True)
    print(parsed_data)
    for time, distance in parsed_data:
        margin *= get_ways_to_win(time, distance)
    return margin


with open('./input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(get_product_of_winning_ways(lines))
