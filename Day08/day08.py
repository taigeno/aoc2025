from itertools import combinations
from collections import defaultdict
import math

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def get_distance(pair):
    p1 = [int(n) for n in pair[0].split(',')]
    p2 = [int(n) for n in pair[1].split(',')]
    
    return math.dist(p1, p2)

def part_one():
    dists = defaultdict(str)
    boxes = defaultdict(set)
    lookup = defaultdict(int)

    for pair in combinations(lines, 2):
        dists[get_distance(pair)] = pair
    
    for i, item in enumerate(lines):
        boxes[i].add(item)
        lookup[item] = i
        
    max = 1000
    for i, item in enumerate(sorted(dists)):
        if i == max:
            break
        p1 = dists[item][0]
        p2 = dists[item][1]

        p1_box = lookup[p1]
        p2_box = lookup[p2]

        if p1_box == p2_box:
            continue

        for item in boxes[p2_box]:
            boxes[p1_box].add(item)
            lookup[item] = p1_box
        del boxes[p2_box]

    total = 1
    for i, b in enumerate(sorted(boxes, key=lambda k: len(boxes[k]), reverse=True)):
        if i == 3:
            break
        total *= len(boxes[b])
    
    print(total)

def part_two():
    dists = defaultdict(str)
    boxes = defaultdict(set)
    lookup = defaultdict(int)
    
    for pair in combinations(lines, 2):
        dists[get_distance(pair)] = pair

    for i, item in enumerate(lines):
        boxes[i].add(item)
        lookup[item] = i

    last_pair = {}
    for item in sorted(dists):
        if len(boxes) == 1:
            break

        p1 = dists[item][0]
        p2 = dists[item][1]

        last_pair = (p1, p2)

        p1_box = lookup[p1]
        p2_box = lookup[p2] 

        if p1_box == p2_box:
            continue

        for item in boxes[p2_box]:
            boxes[p1_box].add(item)
            lookup[item] = p1_box
        del boxes[p2_box]

    print(last_pair)
    print(int(last_pair[0].split(',')[0]) * int(last_pair[1].split(',')[0]))

part_one()
part_two()
