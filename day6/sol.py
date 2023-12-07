import re
from math import sqrt, ceil
from functools import reduce


def parse_file(lines: list[str]):
    # part 1 input
    times = list(map(lambda x: int(x), re.findall(r'\d+', lines[0])))
    distances = list(map(lambda x: int(x), re.findall(r'\d+', lines[1])))
    # part 2 input
    time = [int(reduce(lambda a,b: a + b, map(lambda x: str(x), times)))]
    distance = [int(reduce(lambda a,b: a + b, map(lambda x: str(x), distances)))]

    return zip(times, distances), zip(time, distance)


def solution(data: list[(int, int)], adv=False):
    res = 0 if adv else 1
    for time, distance in data:
        x0, x1 = (-time - sqrt(time**2 - 4*(-1)*(-distance)))/(-2), (-time + sqrt(time**2 - 4*(-1)*(-distance)))/(-2)
        if x0 > x1:
            x0, x1 = x1, x0
        x0, x1 = int(x0 + 1), ceil(x1-1)
        count = x1 - x0 + 1
        res = res + (x1 - x0 + 1) if adv else res * count
    return res





if __name__ == "__main__":
    filename = "./day6/input.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    times_distances, time_distance = parse_file(lines)
    print(solution(times_distances))
    print(solution(time_distance, True))
