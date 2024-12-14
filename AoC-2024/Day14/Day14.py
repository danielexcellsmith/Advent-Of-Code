import re

with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def flatten(xss): # Turn list of lists into 1 list for check sum
    return [x for xs in xss for x in xs]

def part1(puzzle):
    count = [0,0,0,0] # Number in 4 quadrants
    res = 1
    for x, y, vx, vy in re.findall(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', puzzle): # Regex finds initial position [x,y] and velocity [vx,vy]
        x, y = (int(x) + int(vx) * 100) % 101, (int(y) + int(vy) * 100) % 103 # Position after 100 secs
        if x < 50 and y < 51: # Adds each robot to a quadrant
            count[0] += 1
        elif x > 50 and y < 51:
            count[1] += 1
        elif x < 50 and y > 51:
            count[2] += 1
        elif x > 50 and y > 51:
            count[3] += 1
    for a in count:
        res *= a # Multiply together 4 quadrant values
    return res

def part2(puzzle):
    secs = 0
    x_line = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX' # Will be in Christmas tree somewhere
    while True:
        board = []
        for _ in range(103): # Make empty board
            row = []
            for _ in range(101):
                row.append(' ')
            board.append(row)
        for x, y, vx, vy in re.findall(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', puzzle): # Same regex
            x, y = (int(x) + int(vx) * secs) % 101, (int(y) + int(vy) * secs) % 103 # Position each second
            board[y][x] = 'X'
        if re.search(x_line, ''.join(flatten(board))): # Search for long list of X's
            break
        secs += 1
    '''for line in board:
        print(''.join(line))''' # Prints board so I can see if it works
    return secs

print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')