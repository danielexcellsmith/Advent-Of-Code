with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def part1(puzzle):
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    puzzle_list = puzzle.split('\n')
    counter = 0
    for i in range(len(puzzle_list)):
        for j in range(len(puzzle_list[0])):
            if puzzle_list[i][j] == 'X':
                for x in range(8):
                    if i + 3 * directions[x][0] < 0 or j + 3 * directions[x][1] < 0: # out of grid
                        continue
                    elif i + 3 * directions[x][0] >= len(puzzle_list) or j + 3 * directions[x][1] >= len(puzzle_list[0]): # out of grid
                        continue
                    elif ''.join(['X',puzzle_list[i + directions[x][0]][j + directions[x][1]],puzzle_list[i + 2 * directions[x][0]][j + 2 * directions[x][1]],puzzle_list[i + 3 * directions[x][0]][j + 3 * directions[x][1]]]) == 'XMAS':
                        counter += 1
    return counter

def part2(puzzle):
    directions = [(1, 1), (-1, 1)]
    puzzle_list = puzzle.split('\n')
    counter = 0
    for x in range(len(puzzle_list) - 2):
        i = x + 1
        for y in range(len(puzzle_list[0]) - 2):
            j = y + 1
            if puzzle_list[i][j] == 'A':
                if ''.join([puzzle_list[i - directions[0][0]][j - directions[0][1]], 'A',
                                  puzzle_list[i + directions[0][0]][j + directions[0][1]]]) == 'MAS' or ''.join([puzzle_list[i + directions[0][0]][j + directions[0][1]], 'A',
                                  puzzle_list[i - directions[0][0]][j - directions[0][1]]]) == 'MAS':
                    if ''.join([puzzle_list[i - directions[1][0]][j - directions[1][1]], 'A',
                                puzzle_list[i + directions[1][0]][j + directions[1][1]]]) == 'MAS' or ''.join(
                        [puzzle_list[i + directions[1][0]][j + directions[1][1]], 'A',
                         puzzle_list[i - directions[1][0]][j - directions[1][1]]]) == 'MAS':
                        counter += 1
    return counter

print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
