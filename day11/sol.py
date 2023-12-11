def find_empty_rows_and_cols(space: list[list[str]]):
    rows, cols = [], []
    for i, row in enumerate(space):
        flag = False
        for el in row:
            if el != '.':
                flag = True
                break
        if flag: continue
        rows.append(i)
    for i in range(len(space[0])):
        flag = False
        for j in range(len(space)):
            if space[j][i] != '.':
                flag = True
                break
        if flag: continue
        cols.append(i)
    return rows, cols


def find_galaxies(space: list[list[str]]):
    galaxies = []
    for i, row in enumerate(space):
        for j, el in enumerate(row):
            if el == '#':
                galaxies.append((i, j))
    return galaxies
        

def get_in_between(pos1: tuple[int, int], pos2: tuple[int, int], rows: list[int], cols: list[int]):
    count = 0
    for i in range(min(pos1[0], pos2[0]), max(pos1[0], pos2[0]) + 1):
        if i in rows:
            count += 1
    for i in range(min(pos1[1], pos2[1]), max(pos1[1], pos2[1]) + 1):
        if i in cols:
            count += 1
    return count


# an advanced manhattan metric that takes into account multiplied rows and columns
def manhattan_distance(pos1: tuple[int, int], pos2: tuple[int, int], rows: list[int], cols: list[int], scale: int=2):
    in_between_count = get_in_between(pos1, pos2, rows, cols)
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + in_between_count * (scale - 1)


def solution(space: list[list[str]], scale: int=2):
    row_indices, col_indices = find_empty_rows_and_cols(space)
    galaxies = find_galaxies(space)
    res = 0
    for i in range(len(galaxies) - 1):
        for j in range(i+1, len(galaxies)):
            res += manhattan_distance(galaxies[i], galaxies[j], row_indices, col_indices, scale)
    return res



if __name__ == "__main__":
    input_file = './day11/input.txt'
    with open(input_file, 'r') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        for i in range(len(lines)):
            lines[i] = [x for x in lines[i]]

    print(solution(lines))
    print(solution(lines, 1000000))
