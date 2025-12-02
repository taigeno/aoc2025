with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    start = 50
    password = 0
    for line in lines:
        increment = int(line[1:])
        if line[0] == "L":
            start -= increment
        elif line[0] == "R":
            start += increment
        
        # Reset counter to 0-99
        start = start%100

        if start == 0:
            password += 1
        print(start)
    print(password)

def part_two():
    start = 50
    password = 0
    for line in lines:
        increment = int(line[1:])
        
        # Count every extra loops
        password += int(increment/100)
        increment = increment%100

        started_at_zero = start == 0

        if line[0] == "L":
            start -= increment
        elif line[0] == "R":
            start += increment

        # If it's outside of 1-99, it must have crossed 0
        if not started_at_zero and (start < 1 or start > 99):
            password += 1

        # Reset counter to 0-99
        start = start%100

        print(start)
    print(password)
    pass

part_one()
part_two()
