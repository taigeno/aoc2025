with open('input.txt', 'r') as inputFile:
    room = [list(line.strip()) for line in inputFile]

nrows = len(room)
ncols = len(room[0])

def get_cell(row, col):
    if row < 0 or row >= nrows:
        return '.'
    elif col < 0 or col >= ncols:
        return '.'
    else:
        return room[row][col]

def check_cell(row, col):
    sum = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            if get_cell(i, j) == '@':
                sum += 1
    
    if sum < 4:
        return True
    else:
        return False

def check_paper():
    cells = []
    for i in range(nrows):
        for j in range(ncols):
            if get_cell(i, j) == '.':
                continue
            if check_cell(i,j):
                cells.append((i,j))
    return cells

def adjust_grid(cells):
    for cell in cells:
        room[cell[0]][cell[1]] = '.'

def part_one():
    print(len(check_paper()))

def part_two():
    total = 0
    cells = check_paper()

    while len(cells) > 0:
        total += len(cells)
        adjust_grid(cells)
        cells = check_paper()
    
    print(total)

part_one()
part_two()
