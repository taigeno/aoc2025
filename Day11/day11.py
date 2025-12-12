with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def count_paths(graph, start, end):
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
    print(count_paths(servers, "you", "out"))

def part_two():
    # None go from "dac" to "fft"
    print(count_paths(servers, "svr", "fft") * count_paths(servers, "fft", "dac") * count_paths(servers, "dac", "out"))

part_one()
part_two()
