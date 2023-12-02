from functools import reduce


digit_map = {
    # 'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

words = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}


def make_digits(line: str):
    n = len(line)
    for word in words:
        i = 0
        while i <= n and i > -1:
            index = line.find(word, i)
            if index != -1:
                line = line[:index+len(word)//2] + digit_map[word] + line[index+len(word)//2+1:]
            i = index
    return line


def sum_coords(lines: list[str], adv: bool=False):
    res = 0
    for line in lines:
        if adv:
            line = make_digits(line)
        numbers = list(filter(lambda c: str.isdigit(c), line))
        number = numbers[0] + numbers[-1]
        res += int(number)
    return res



if __name__ == "__main__":
    input_file = './input.txt'
    with open(input_file, 'r') as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    print(sum_coords(lines))
    print(sum_coords(lines, True))