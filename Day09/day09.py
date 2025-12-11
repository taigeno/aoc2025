from itertools import combinations

from shapely.geometry import Polygon, box

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def get_points(pair):
    return [int(n) for n in pair[0].split(",")], [int(n) for n in pair[1].split(",")]

def get_area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    
def part_one():
    areas = [get_area(*get_points(pair)) for pair in combinations(lines, 2)]
    
    print(max(areas))

def rectangle_is_in_polygon(pair, p):
    p1, p2 = get_points(pair)
    
    x1, y1 = p1
    x2, y2 = p2

    rectangle = box(
        min(x1, x2), min(y1, y2), 
        max(x1, x2), max(y1, y2)
    )

    if p.contains(rectangle):
        return get_area(p1, p2)
    else:
        return 0
    
def part_two():
    pts = [(int(x) for x in line.split(",")) for line in lines]

    p = Polygon(pts)

    pair_to_areas = dict()
    for pair in combinations(lines, 2):
        p1, p2 = get_points(pair)
        pair_to_areas[pair] = get_area(p1, p2)
    
    for pair in sorted(pair_to_areas, key=lambda k: pair_to_areas[k], reverse=True):
        if rectangle_is_in_polygon(pair, p):
            print("found", pair, pair_to_areas[pair])
            break

part_one()
part_two()
