import math

with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def part1(puzzle):
    puzzle_list = puzzle.split('\n')
    puzzle_matrix = []
    antinode_grid = []
    for line in puzzle_list:
        puzzle_matrix.append(list(line))
        antinode_grid.append(['.'] * len(line))
    for y1 in range(len(puzzle_matrix)):
        for x1 in range(len(puzzle_matrix[0])):
            if puzzle_matrix[y1][x1] == '.':
                continue
            for y2 in range(len(puzzle_matrix)):
                for x2 in range(len(puzzle_matrix[0])):
                    y_new, x_new = 2 * y2 - y1, 2 * x2 - x1
                    if y_new < 0 or x_new < 0 or y_new >= len(puzzle_matrix) or x_new >= len(puzzle_matrix[0]):
                        continue
                    if y1 == y2 and x1 == x2:
                        continue
                    if puzzle_matrix[y2][x2] == puzzle_matrix[y1][x1]:
                        antinode_grid[y_new][x_new] = '#'
    counter = 0
    for line in antinode_grid:
        for char in line:
            if char == '#':
                counter += 1
    return counter

def part2(puzzle):
    puzzle_list = puzzle.split('\n')
    puzzle_matrix = []
    antinode_grid = []
    for line in puzzle_list:
        puzzle_matrix.append(list(line))
        antinode_grid.append(['.'] * len(line))
    for y1 in range(len(puzzle_matrix)):
        for x1 in range(len(puzzle_matrix[0])):
            if puzzle_matrix[y1][x1] == '.':
                continue
            for y2 in range(len(puzzle_matrix)):
                for x2 in range(len(puzzle_matrix[0])):
                    if y1 == y2 and x1 == x2:
                        continue
                    dist_norm = math.sqrt(pow(y2 - y1, 2) + pow(x2 - x1, 2))
                    if puzzle_matrix[y2][x2] == puzzle_matrix[y1][x1]:
                        if x2 == x1:
                            m = 'inf'
                        else:
                            m = (y2 - y1) / (x2 - x1)
                        antinode_grid[y1][x1] = '#'
                        antinode_grid[y2][x2] = '#'
                        for y_new in range(len(puzzle_matrix)):
                            for x_new in range(len(puzzle_matrix[0])):
                                if x_new == x2:
                                    m_new = 'inf'
                                else:
                                    m_new = (y_new - y2)/(x_new - x2)
                                if m_new == m:
                                    antinode_grid[int(y_new)][int(x_new)] = '#'

    counter = 0
    for line in antinode_grid:
        for char in line:
            if char == '#':
                counter += 1
    return counter

print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')