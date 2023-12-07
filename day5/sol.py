import re


def parse_input(lines: list[str]) -> (list[int], list[dict]):
    seeds = list(map(lambda x: int(x), re.findall(r'\d+', lines[0].split(":")[1])))
    maps = []

    # first two lines are inconsequential for maps
    for line in lines[2:]:
        if not line:
            continue
        if not re.findall(r'\d+', line):
            maps.append(dict())
            continue

        destination, source, length = list(map(lambda x: int(x), line.split()))
        maps[-1][(source, source + length - 1)] = (destination, destination + length - 1)
    return seeds, maps
        

def get_destination(custom_map: dict[(int, int), (int, int)], index, reverse=False):
    for source_range, destination_range in custom_map.items():
        if reverse:
            source_range, destination_range = destination_range, source_range
        if source_range[0] <= index <= source_range[1]:
            diff = index - source_range[0]
            return destination_range[0] + diff
    return index
        


def part_1(seeds: list[int], maps: list[dict]):
    result = float('+inf')
    for seed in seeds:
        mapped_seed = seed
        for custom_map in maps:
            mapped_seed = get_destination(custom_map, mapped_seed)
        if mapped_seed < result:
            result = mapped_seed
    return result


# brute force approach
def part_2(seed_ranges: list[(int, int)], maps: list[dict]):
    for i in range(max(seed_ranges, key=lambda x: x[1])[1]):
        index = i
        for curr_map in reversed(maps):
            index = get_destination(curr_map, index, True)
        for seed_range in seed_ranges:
            if seed_range[0] <= index <= seed_range[1]:
                return i
    return -1



if __name__ == "__main__":
    filename = "./day5/input.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    seeds, maps = parse_input(lines)
    seed_ranges = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]
    print(part_1(seeds, maps))
    print(part_2(seed_ranges, maps))
