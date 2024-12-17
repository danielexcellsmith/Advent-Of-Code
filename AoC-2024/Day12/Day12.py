from collections import deque

with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def bfs(maze, start):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    perimeter = 0
    while queue:
        current = queue.popleft()
        current_letter = maze[current[0]][current[1]]
        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= next_cell[0] < len(maze) and
                    0 <= next_cell[1] < len(maze[0]) and
                    maze[next_cell[0]][next_cell[1]] == current_letter):
                if next_cell not in visited:
                    queue.append(next_cell)
                    visited.add(next_cell)
            else:
                perimeter += 1
    corners = 0
    for item in visited:
        for direction in directions:
            next_cell = (item[0] + direction[0], item[1] + direction[1])
            extra_cell = (item[0] + directions[directions.index(direction) - 1][0],
                          item[1] + directions[directions.index(direction) - 1][1])
            diagonal_cell = (item[0] + direction[0] + directions[directions.index(direction) - 1][0],
                             item[1] + direction[1] + directions[directions.index(direction) - 1][1])
            if next_cell not in visited and extra_cell not in visited:
                corners += 1
            if next_cell in visited and extra_cell in visited and diagonal_cell not in visited:
                corners += 1
    return visited, perimeter, corners

def part1part2(puzzle):
    puzzle_matrix = []
    for line in puzzle.split('\n'):
        puzzle_matrix.append(list(line))
    visited = set()
    part1 = 0
    part2 = 0
    for i in range(len(puzzle_matrix)):
        for j in range(len(puzzle_matrix[0])):
            if (i,j) in visited:
                continue
            new_visited, perimeter, corners = bfs(puzzle_matrix, (i,j))
            visited.update(new_visited)
            part1 += len(new_visited) * perimeter
            part2 += len(new_visited) * corners
    return part1, part2

print(f'Part 1: {part1part2(puzzle_input)[0]}')
print(f'Part 2: {part1part2(puzzle_input)[1]}')