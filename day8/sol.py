from functools import reduce


def parse_file(lines: list[str]):
    path = lines[0]
    lines = lines[2:]
    graph = dict()

    for line in lines:
        source, targets = line.split(" = ")
        targets = targets.strip('()').split(', ')
        graph[source] = targets
    return path, graph


def check_all_nodes(nodes: list[str]):
    for node in nodes:
        if node[-1] != 'Z': return False
    return True


def gcd(a: int, b: int):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def lcm(a: int, b: int):
    return abs(a * (b / gcd(a, b)))


def lcmm(*args):
    return reduce(lcm, args)


def sol(path: str, graph: dict(), adv=True):
    i, n = 0, len(path)
    if adv:
        curr_nodes = [k for k in graph.keys() if k[-1] == 'A']
    else:
        curr_nodes = ['AAA']
    counters = [0 for _ in range(len(curr_nodes))]

    for i, node in enumerate(curr_nodes):
        curr_node = node
        j = 0
        while curr_node[-1] != 'Z':
            counters[i] += 1
            if path[j] == 'L':
                curr_node = graph[curr_node][0]
            else:
                curr_node = graph[curr_node][1]
            j = (j + 1) % n
        
    return int(lcmm(*counters)) if adv else counters[i]



if __name__ == "__main__":
    input_file = './day8/input.txt'
    with open(input_file, 'r') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))

    path, graph = parse_file(lines)
    
    print(sol(path, graph, False))
    print(sol(path, graph))