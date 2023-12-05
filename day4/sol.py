import re


def find_matches(line, mult=True):
    numbers_matching = 0
    parts = line.split('|')
    winning_numbers = list(map(lambda x: int(x), re.findall(r'\d+', parts[0].split(':')[1])))
    player_numbers = list(map(lambda x: int(x), re.findall(r'\d+', parts[1])))

    for p_num in player_numbers:
        if p_num in winning_numbers:
            if mult:
                numbers_matching = 1 if numbers_matching == 0 else numbers_matching * 2
            else:
                numbers_matching += 1
    return numbers_matching


def part_1(lines: list[str]):
    counter = 0
    for line in lines:
        numbers_matching = find_matches(line)
        counter += numbers_matching
    return counter


def part_2(lines: list[str]):
    card_counts = dict([(i, 1) for i in range(len(lines))])
    counter = 0

    for i, line in enumerate(lines):
        numbers_matching = find_matches(line, False)
        for j in range(i+1, i+numbers_matching+1):
            if j < len(lines):
                card_counts[j] += card_counts[i]
        counter += card_counts[i]
    return counter
            



if __name__ == "__main__":
    filename = "./day4/input.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    print(part_1(lines))
    print(part_2(lines))