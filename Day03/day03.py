from collections import deque

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    sum = 0
    for line in lines:
        sum += find_joltage(line)
    print(sum)

def find_joltage(line):
    max_ten = 0
    max_one = 0

    for i, d in enumerate(reversed(line)):
        digit = int(d)
        if i == 0:
            max_one = digit
            continue

        if digit >= max_ten:
            max_one = max(max_ten, max_one)
            max_ten = digit

    return max_ten * 10 + max_one

def part_two():
    n = 12
    sum = 0
    for line in lines:
        sum += find_joltage_n(line, n)
    print(sum)

def find_joltage_n(line, n):
    j = deque([])

    for i, d in enumerate(reversed(line)):
        digit = int(d)
        if i < n:
            j.appendleft(digit)
            continue

        temp = digit
        for ii, x in enumerate(j):
            if temp >= x:
                j[ii] = temp
                temp = x
            else:
                break

    return int("".join(map(str,j)))

part_one()
part_two()
