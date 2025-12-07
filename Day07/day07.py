from collections import defaultdict

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    num_splits = 0
    rays = set()
    rays.add(lines[0].index("S"))
    for line in lines[1:]:
        for ray in list(rays):
            if line[ray] =="^":
                rays.add(ray - 1)
                rays.add(ray + 1)
                rays.remove(ray)
                num_splits += 1

    print(num_splits)

def part_two():
    rays = defaultdict(int)
    rays[lines[0].index("S")] = 1
    for line in lines[1:]:
        for ray in list(rays):
            if line[ray] =="^":
                rays[ray - 1] += rays[ray]
                rays[ray + 1] += rays[ray]
                del rays[ray]

    print(sum(rays.values()))

part_one()
part_two()
