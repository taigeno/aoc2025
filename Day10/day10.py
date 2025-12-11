import numpy as np
from scipy.optimize import linprog

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def process_line(line):
    args = line.split()
    indicator = [i for i, ind in enumerate(args[0][1:-1]) if ind == "#"]
    schematic = [tuple(int(n) for n in s[1:-1].split(",")) for s in args[1:-1]]
    joltage = [int(j) for j in args[-1][1:-1].split(",")]

    return indicator, schematic, joltage

def get_num_presses(indicator, schematic):
    goal = tuple(indicator)
    buttons = set(schematic)

    progress = buttons
    
    cycles = 1
    while True:
        for p in progress:
            if p == goal:
                return cycles
            
        cycles += 1
        new_progress = set()
        for p in progress:
            for b in buttons:
                new_progress.add(tuple(set(p) ^ set(b)))
        progress = new_progress

def part_one():
    total = 0
    for line in lines:
        indicator, schematic, _ = process_line(line)
        total += get_num_presses(indicator, schematic)
    print(total)

def get_num_presses_joltage(joltage, schematic):
    buttons = [[1 if i in s else 0 for s in schematic] for i, _ in enumerate(joltage)]

    A = np.array(buttons)

    b = np.array(joltage)

    c = np.array([1] * len(schematic))

    x = linprog(c, A_eq=A, b_eq=b, integrality=1)
    print("answer", x.x)

    return np.sum(x.x)

def part_two():
    total = 0
    for line in lines:
        _, schematic, joltage = process_line(line)
        print(joltage, schematic)
        total += get_num_presses_joltage(joltage, schematic)
    
    print(total)

part_one()
part_two()
