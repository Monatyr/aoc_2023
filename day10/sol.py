class Pos:
    def __init__(self, pos: tuple[int, int]):
        self.pos = pos

    def __add__(self, other):
        return Pos((self.pos[0] + other.pos[0], self.pos[1] + other.pos[1]))


# get direction based on the pipe type and the previous position change
move_dict = {
    '|': {(1, 0): (1, 0), (-1, 0): (-1, 0)},
    '-': {(0, 1): (0, 1), (0, -1): (0, -1)},
    'L': {(1, 0): (0, 1), (0, -1): (-1, 0)},
    'J': {(0, 1): (-1, 0), (1, 0): (0, -1)},
    '7': {(0, 1): (1, 0), (-1, 0): (0, -1)},
    'F': {(-1, 0): (0, 1), (0, -1): (1, 0)}
}

corner_dict = {
    (-1, -1): 'F',
    (-1, 1): '7',
    (1, -1): 'L',
    (1, 1): 'J'
}

up = {'|', '7', 'F'}
down = {'|', 'L', 'J'}
left = {'-', 'L', 'F'}
right = {'-', '7', 'J'}


def get_starting_pipe(pipes: list[str], start_pos: tuple[int , int]):
    h, w = len(pipes), len(pipes[0])
    vertical, horizontal = 0, 0
    res = Pos((0, 0))
    
    if start_pos[0] - 1 >= 0 and pipes[start_pos[0] - 1][start_pos[1]] in up:
        res += Pos((1, 0))
        vertical += 1
    if start_pos[0] + 1 < h and pipes[start_pos[0] + 1][start_pos[1]] in down:
        res += Pos((-1, 0))
        vertical += 1
    if start_pos[1] - 1 >= 0 and pipes[start_pos[0]][start_pos[1] - 1] in left:
        res += Pos((0, 1))
        horizontal += 1
    if start_pos[1] + 1 < w and pipes[start_pos[0]][start_pos[1] + 1] in right:
        res += Pos((0, -1))
        horizontal += 1

    if vertical == 2:
        return '|'
    if horizontal == 2:
        return '-'
    return corner_dict[res.pos]     


def find_start(pipes: list[str]) -> tuple[int, int]:
    for i, row in enumerate(pipes):
        for j, pipe in enumerate(row):
            if pipe == 'S':
                return (i, j)
    return (-1 , -1)


def get_entire_path(pipes: list[str], start_pos: tuple[int, int], first_move: tuple[int, int]):
    curr_pos = Pos(start_pos)
    last_move = first_move
    path = []

    while curr_pos.pos != start_pos or not path:
        last_move = move_dict[pipes[curr_pos.pos[0]][curr_pos.pos[1]]][last_move]
        curr_pos += Pos(last_move)
        path.append(curr_pos.pos)
    return path


def check_direction(pipes: list[str], pos: tuple[int, int], direction: tuple[int, int], path: set[tuple[int, int]]):
    h, w = len(pipes), len(pipes[0])
    curr_pos = Pos(pos)
    last_el = None
    counter = 0
    while 0 <= curr_pos.pos[0] < h and 0 <= curr_pos.pos[1] < w:
        if curr_pos.pos in path:
            symbol = pipes[curr_pos.pos[0]][curr_pos.pos[1]]
            if direction[0] == 1:
                if symbol in ['L', 'F', '-']:
                    counter += 1
            if direction[0] == -1:
                if symbol in ['7', 'J', '-']:
                    counter += 1
            if direction[1] == 1:
                if symbol in ['J', 'L', '|']:
                    counter += 1
            if direction[1] == -1:
                if symbol in ['F', '7', '|']:
                    counter += 1
        curr_pos += Pos(direction) 
    return counter % 2


def prune_grid(pipes: list[str], path: set[tuple[int, int]]):
    h, w = len(pipes), len(pipes[0])
    counter = 0
    res = set()

    for i in range(h):
        for j in range(w):
            if (i, j) not in path:
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dir in directions:
                    if check_direction(pipes, (i, j), dir, path) == 1:
                        # print(i, j, dir)
                        res.add((i, j))
                        counter += 1
                        break
    return counter, res


c_dict = {
    '|': '│',
    '-': '─',
    'F': '┌',
    'L': '└',
    'J': '┘',
    '7': '┐',
    '.': '.'
}

def pretty_grid(pipes: list[str], path: set[tuple[int, int]], inside_elems: set[tuple[int, int]]):
    res = []
    for i in range(len(pipes)):
        res.append([])
        for j in range(len(pipes[0])):
            c = c_dict[pipes[i][j]]
            res[i].append(c)
    for i, row in enumerate(res):
        for j, el in enumerate(row):
            if (i, j) in inside_elems:
                print(f'\033[31m{el}\033[00m', end='')
            elif (i, j) in path:
                print(f'\033[93m{el}\033[00m', end='')
            else:
                print(el, end='')
        print()



if __name__ == "__main__":
    input_file = "./day10/input.txt"
    with open(input_file, 'r') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
    
    start_pos = find_start(lines)
    start_pipe = get_starting_pipe(lines, start_pos)

    # fill in the missing pipeline
    lines = [[c if c != 'S' else start_pipe for c in row] for row in lines]
    
    # arbitrarily chosen direction of the first move
    first_move = list(move_dict[start_pipe].keys())[0]
    path = get_entire_path(lines, start_pos, first_move)
    
    # part 1
    print(len(path)//2)

    # part 2
    path_nodes = set(path)
    res, inside_elems = prune_grid(lines, path_nodes)
    print(res)

    # terminal visualisation
    pretty_grid(lines, path_nodes, inside_elems)
