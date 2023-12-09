def find_differences(numbers: list[int]):
    return [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]


def all_zero(numbers: list[int]):
    for n in numbers:
        if n != 0:
            return False
    return True


def solution(lines: list[str], backwards=False):
    res = 0
    for line in lines:
        numbers = list(map(lambda x: int(x), line.split()))
        differences = [numbers]
        
        while not all_zero(differences[-1]):
            differences.append(find_differences(differences[-1]))

        for i in range(len(differences)-1, 0, -1):
            if backwards:
                base_num = differences[i-1][0] - differences[i][0]
            else:
                base_num = differences[i-1][-1] + differences[i][-1]

            index = 0 if backwards else len(differences[i-1])
            differences[i-1].insert(index, base_num)
        res += differences[0][0 if backwards else -1]
    return res

        


if __name__ == "__main__":
    input_file = "./day9/input.txt"
    with open(input_file, 'r') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
    
    print(solution(lines))
    print(solution(lines, True))