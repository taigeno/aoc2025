with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    ranges = lines[0].split(",")
    total = 0
    for r in ranges:
        ids = r.split("-")
        for id in range(int(ids[0]), int(ids[1]) + 1):
            if is_invalid(id):
                total += id
    print(total)

def is_invalid(id):
    sid = str(id)
    l = len(sid)
    if l == 1:
        return False
    else: # Left half equals right half
        return sid[:l//2] == sid[l//2:]

def part_two():
    ranges = lines[0].split(",")
    total = 0
    for r in ranges:
        ids = r.split("-")
        for id in range(int(ids[0]), int(ids[1]) + 1):
            if is_invalid_2(id):
                total += id
    print(total)

def is_invalid_2(id):
    sid = str(id)
    l = len(sid)
    if l == 1:
        return False
    else:
        for r in range(1, l//2 + 1):
            if l%r == 0 and l//r * sid[:r] == sid:
                return True
        return False

part_one()
part_two()
