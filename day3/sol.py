def find_whole_number(engine: list[str], w, i, j) -> (int, int):
    '''Returns the number of digits that come after the one at the (i,j) position and the number itself'''
    index = j
    num_start = index
    while index >= 0 and engine[i][index].isdigit():
        num_start = index
        index -= 1    
    index = j
    while index < w and engine[i][index].isdigit():
        index += 1
    return (int(engine[i][num_start:index]), index - j)


def check_surroundings(engine: list[str], h, w, num_i, num_j):
    '''Check if number is a part-number; also return its length'''
    number, number_len = find_whole_number(engine, w, num_i, num_j)
    for i in range(num_i-1, num_i+2):
        for j in range(num_j-1, num_j+number_len+1):
            if i == num_i and num_j <= j < num_j + number_len:
                continue
            if 0 <= i < h and 0 <= j < w and engine[i][j] != '.':
                return (number, number_len)
    return (0, number_len)



def part_1(engine: list[str]):
    h = len(engine)
    w = len(engine[0])
    i = 0
    result = 0

    while i < h:
        j = 0
        while j < w:
            if engine[i][j].isdigit():
                number, number_len = check_surroundings(engine, h, w, i, j)
                result += number
                j += number_len
            else:
                j += 1
        i += 1
    return result

#-------------------------------

def gear_surroundings(engine: list[str], h, w, gear_i, gear_j) -> int:
    result_list = []
    for i in range(gear_i - 1, gear_i + 2):
        j = gear_j - 1
        while j < gear_j + 2:
            if engine[i][j].isdigit():
                number, number_len = find_whole_number(engine, w, i, j)
                result_list.append(number)
                j += number_len
            else:
                j+= 1
    return result_list[0] * result_list[1] if len(result_list) == 2 else 0


def part_2(engine: list[str]):
    h = len(engine)
    w = len(engine[0])
    i = 0
    result = 0

    for i in range(h):
        for j in range(w):
            if engine[i][j] == '*':
                result += gear_surroundings(engine, h, w, i, j)
    return result



if __name__ == "__main__":
    with open('./day3/input.txt', 'r') as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(), lines))
    
    print(part_1(lines))
    print(part_2(lines))