with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def check_line(line):
    inputs = line.split(": ")
    x, y = inputs[0].split("x")
    area = int(x) * int(y)

    count = sum(int(n) * 7 for n in inputs[1].split())
    return area >= count

def part_one():
    total = sum([check_line(line) for line in lines if "x" in line])
    print(total)

part_one()
