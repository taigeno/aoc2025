from collections import defaultdict

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    ids = defaultdict(list)
    index = set()
    count = 0
    for line in lines:
        if line == "":
            continue
        elif "-" in line:
            ranges = line.split("-")
            ids[int(ranges[0])].append(int(ranges[1]))
            index.add(int(ranges[0]))
        else:
            num = int(line)
            found = False
            for x in sorted(index):
                for y in ids[x]:
                    if x <= num and num <= y:
                        count += 1
                        break
                else:
                    continue
                break
    print(count)

def part_two():
    ids = defaultdict(list)
    index = set()
    counter = 0
    total = 0
    for line in lines:
        if line == "":
            continue
        elif "-" in line:
            ranges = line.split("-")
            ids[int(ranges[0])].append(int(ranges[1]))
            index.add(int(ranges[0]))

    for x in sorted(index):
        y = max(ids[x])
        if x > counter:
            total += y - x + 1
            counter = y
        elif counter < y and counter >= x:
            total += y - counter
            counter = y
    print(total)

part_one()
part_two()
