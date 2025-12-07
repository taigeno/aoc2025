from functools import reduce
import operator

with open('input.txt', 'r') as inputFile:
    lines = [line.rstrip("\n") for line in inputFile]

def part_one():
    cols = []
    for i, line in enumerate(lines):
        nums = line.strip().split()
        if i == 0:
            for num in nums:
                cols.append([num])
        else:
            for j, num in enumerate(nums):
                cols[j].append(num)
    
    total = 0
    for col in cols:
        if col[-1] == "+":
            total += sum([int(num) for num in col[:-1]])
        elif col[-1] == "*":
            total += reduce(operator.mul, [int(num) for num in col[:-1]], 1)
    
    print(total)

def process_nums(nums, char):
    if char == "+":
        return sum([int(n.strip()) for n in nums if n.strip() != ""])
    elif char == "*":
        return reduce(operator.mul, [int(n.strip()) for n in nums if n.strip() != ""], 1)
            
def part_two():
    total = 0
    nums = []
    index = 0

    # Iterate backwards through the last row of operators
    for i, char in enumerate(reversed(lines[-1])):
        # Collect numbers by column from the back
        for j, row in enumerate(lines[:-1]):
            if j == 0:
                nums.append(row[-1*(i+1)])
            else:
                nums[index] += row[-1*(i+1)]
        index += 1

        # Calculate total and reset nums when we hit an operator
        if char == "+" or char == "*":
            total += process_nums(nums, char)
            nums = []
            index = 0

    print(total)

part_one()
part_two()
