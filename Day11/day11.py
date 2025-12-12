with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def count_paths_graph(graph, start, end):
    memo = {}

    def dfs(node):
        if node == end:
            return 1
        
        if node in memo:
            return memo[node]
        
        count = 0
        for neighbor in graph.get(node, []):
            count += dfs(neighbor)
        
        memo[node] = count
        return count

    return dfs(start)

servers = {server: outputs.split() for server,outputs in [line.split(": ") for line in lines]}

def part_one():
    print(count_paths_graph(servers, "you", "out"))

def part_two():
    print(count_paths_graph(servers, "svr", "fft") * count_paths_graph(servers, "fft", "dac") * count_paths_graph(servers, "dac", "out"))

part_one()
part_two()
