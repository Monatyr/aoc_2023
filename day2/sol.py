from functools import reduce


cubes_count = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def simple_solution(lines):
    result = 0
    for line in lines:
        flag = True
        game, games_list = line.split(':')
        index = int(game.split(" ")[1])

        game_rounds = games_list.split(';')
        for round in game_rounds:
            color_divided = round.split(',')
            for color in color_divided:
                color = color.strip()
                count, col = int(color.split(' ')[0]), color.split(' ')[1]
                if count > cubes_count[col]:
                   flag = False
                   break
            if not flag: break
        if flag: result += index 
    return result


def advanced_solution(lines):
    result = 0
    for line in lines:
        flag = True
        game, games_list = line.split(':')
        index = int(game.split(" ")[1])

        game_rounds = games_list.split(';')
        color_count = {'red': 0, 'green': 0, 'blue': 0}
        for round in game_rounds:
            color_divided = round.split(',')
            for color in color_divided:
                color = color.strip()
                count, col = int(color.split(' ')[0]), color.split(' ')[1]
                if color_count[col] < count:
                    color_count[col] = count
        set_power = reduce((lambda a, b: a * b), color_count.values())
        result += set_power
    return result


if __name__ == "__main__":
    input_file = './day2/input.txt'
    with open(input_file, 'r') as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(), lines))
    
    print(simple_solution(lines))
    print(advanced_solution(lines))