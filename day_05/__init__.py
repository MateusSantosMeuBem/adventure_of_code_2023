MAP_LABELS = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location',
]


def get_seed_and_maps(read_file: str):
    return read_file.split('\n\n')


def get_seeds(chunk: str):
    return list(map(int, chunk.split(':')[1].split()))


def get_source_destination(chunk: str):
    lines = {}
    for line in chunk.split(':')[1].split('\n'):
        if line.split():
            destination, source, map_range = map(int, line.split())
            lines.update({
                source: (destination, map_range)
            })

    return lines


def get_destination(source: int, current_map: dict[int, tuple[int, int]]):
    source_present_mask = [
        str(s) if source >= s and source < s + l else False
        for s, (_, l) in current_map.items()
    ]
    is_mapped = any(source_present_mask)
    destination = source
    if is_mapped:
        s = int(list(filter(lambda x: x != False, source_present_mask))[0])
        d, _ = current_map[s]
        destination = abs(source - s) + d
    return destination


def get_closest_destination(read_file: str):
    chunks = get_seed_and_maps(read_file)
    seeds = get_seeds(chunks[0])
    maps = {}
    for index, map_label in enumerate(MAP_LABELS, start=1):
        maps[map_label] = get_source_destination(chunks[index])

    locations = []
    for seed in seeds:
        previous = get_destination(seed, maps['seed-to-soil'])
        previous = get_destination(previous, maps['soil-to-fertilizer'])
        previous = get_destination(previous, maps['fertilizer-to-water'])
        previous = get_destination(previous, maps['water-to-light'])
        previous = get_destination(previous, maps['light-to-temperature'])
        previous = get_destination(previous, maps['temperature-to-humidity'])
        locations.append(get_destination(
            previous, maps['humidity-to-location']))
    return min(locations)


with open(r'C:\Users\Mateus\projects\python\adventure_of_code_23\day_05\input.txt', 'r', encoding='utf-8') as file:
    read_file = file.read()

print(get_closest_destination(read_file))
