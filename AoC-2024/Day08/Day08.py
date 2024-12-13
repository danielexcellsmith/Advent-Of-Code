with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def part1(puzzle):
    puzzle_list = puzzle.split('\n')
    puzzle_matrix = []
    antinode_grid = []
    for line in puzzle_list:
        puzzle_matrix.append(list(line)) # Make list of lists grid
        antinode_grid.append(['.'] * len(line)) # Make grid for antinodes
    for y1 in range(len(puzzle_matrix)):
        for x1 in range(len(puzzle_matrix[0])): # Iterate through all points in grid
            if puzzle_matrix[y1][x1] == '.': # Skip if '.'
                continue
            for y2 in range(len(puzzle_matrix)):
                for x2 in range(len(puzzle_matrix[0])): # Iterate to find matching symbols
                    y_new, x_new = 2 * y2 - y1, 2 * x2 - x1
                    if y_new < 0 or x_new < 0 or y_new >= len(puzzle_matrix) or x_new >= len(puzzle_matrix[0]):
                        continue # Don't leave grid
                    if y1 == y2 and x1 == x2: # Don't place antinode where antennae are
                        continue
                    if puzzle_matrix[y2][x2] == puzzle_matrix[y1][x1]: # If symbols match
                        antinode_grid[y_new][x_new] = '#'
    counter = 0
    for line in antinode_grid:
        for char in line:
            if char == '#': # Count number of '#' in new grid
                counter += 1
    return counter

def part2(puzzle):
    puzzle_list = puzzle.split('\n')
    puzzle_matrix = []
    antinode_grid = []
    for line in puzzle_list: # Same as part 1
        puzzle_matrix.append(list(line))
        antinode_grid.append(['.'] * len(line))
    for y1 in range(len(puzzle_matrix)):
        for x1 in range(len(puzzle_matrix[0])): # Same as part 1
            if puzzle_matrix[y1][x1] == '.':
                continue
            for y2 in range(len(puzzle_matrix)):
                for x2 in range(len(puzzle_matrix[0])):
                    if y1 == y2 and x1 == x2:
                        continue
                    if puzzle_matrix[y2][x2] == puzzle_matrix[y1][x1]:
                        antinode_grid[y1][x1] = '#' # Now place antinodes where antennae are
                        antinode_grid[y2][x2] = '#'
                        if x2 == x1: # Infinite edge case
                            m = 'inf'
                        else:
                            m = (y2 - y1) / (x2 - x1) # Finding gradient between antennae
                        for y_new in range(len(puzzle_matrix)):
                            for x_new in range(len(puzzle_matrix[0])): # Iterate through the grid again
                                if x_new == x2:
                                    m_new = 'inf'
                                else:
                                    m_new = (y_new - y2)/(x_new - x2)
                                if m_new == m: # If gradient between antennae = gradient between antenna and antinode
                                    antinode_grid[int(y_new)][int(x_new)] = '#'

    counter = 0
    for line in antinode_grid:
        for char in line:
            if char == '#':
                counter += 1
    return counter

print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
